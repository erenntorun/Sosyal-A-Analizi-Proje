#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 00:50:41 2024

@author: eren
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import os
import community as community_louvain



def oynanma_sayıları(df):
    
    ajan_oynanma_sayısı = df['agent'].value_counts()    
    harita_oynanma_sayısı = df['map'].value_counts()
    ajan_harita_oynanma_sayısı = df.groupby(['map', 'agent']).size().reset_index(name='oynanma sayısı')
    
    print("Ajan Oynanma Sayısı:")
    print(ajan_oynanma_sayısı)

    print("\nHarita Oynanma Sayısı:")
    print(harita_oynanma_sayısı)

    print("\nAjanların Haritada Oynanma Sayısı:")
    print(ajan_harita_oynanma_sayısı)

    return ajan_harita_oynanma_sayısı,harita_oynanma_sayısı,ajan_oynanma_sayısı


def grafikler(df):
    
    harita_ajan_ciftleri = df[['map', 'agent']].values
    G_ag = nx.Graph()  

    haritalar = df['map'].unique() 
    ajanlar = df['agent'].unique()

    G_ag.add_nodes_from(haritalar, type='map') 
    G_ag.add_nodes_from(ajanlar, type='agent')

    oynanma_sayilari = df.groupby(['map', 'agent']).size().reset_index(name='oynanma sayısı')

    for harita, ajan in harita_ajan_ciftleri:

        oynanma_sayisi = oynanma_sayilari[(oynanma_sayilari['map'] == harita) & (oynanma_sayilari['agent'] == ajan)]['oynanma sayısı'].values[0]
        G_ag.add_edge(harita, ajan, weight=oynanma_sayisi)

    plt.figure(figsize=(40, 30))
    pos = nx.spring_layout(G_ag, seed=42)
    node_colors = ['lightcoral' if G_ag.nodes[node]['type'] == 'map' else 'lightblue' for node in G_ag]

    nx.draw(
        G_ag, pos, with_labels=True, node_color=node_colors,
        edge_color='gray', node_size=2000, font_size=10, font_weight='bold'
    )

    edge_labels = nx.get_edge_attributes(G_ag, 'weight')
    nx.draw_networkx_edge_labels(
        G_ag, pos, edge_labels=edge_labels, font_size=10, font_color='red'
    )

    plt.title("Ağırlıklı Harita-Ajan İlişki Ağı")
    plt.show()

    plt.figure(figsize=(20, 8))
    ax = sns.countplot(y='agent', data=df, order=df['agent'].value_counts().index, palette='deep')
    plt.xlabel('Oynanma Sayıları')
    plt.ylabel('Ajanlar')
    plt.title('Ajanların Oynanma Sayıları')
    
    for p in ax.patches:
        ax.annotate(f'{p.get_width()}', (p.get_x() + p.get_width(), p.get_y() + p.get_height()/2),
                    ha='center', va='center', size=12, color='black', xytext=(10, 0), textcoords='offset points')
    plt.show()

    plt.figure(figsize=(8, 4))
    ax = sns.countplot(data=df, y='map', hue='map', order=df['map'].value_counts().index, palette='deep')
    plt.xlabel('Oynanma Sayıları')
    plt.ylabel('Haritalar')
    plt.title('Haritaların Oynanma Sayıları')

    for p in ax.patches:
        ax.annotate(f'{p.get_width()}', (p.get_x() + p.get_width(), p.get_y() + p.get_height()/2),
                    ha='center', va='center', size=12, color='black', xytext=(10, 0), textcoords='offset points')
    plt.show()

    return G_ag


def ag_ozellikleri(G):
    
    derece_merkezilik = nx.degree_centrality(G)
    
    betweenness_merkezilik = nx.betweenness_centrality(G, weight='weight')

    closeness_merkezilik = nx.closeness_centrality(G)
    
    ozellikler_df = pd.DataFrame({
        'Derece Merkeziliği': derece_merkezilik,
        'Arasındalık Merkeziliği': betweenness_merkezilik,
        'Yakınlık Merkeziliği': closeness_merkezilik
    })
    
    return ozellikler_df


def ag_ozelliklerini_gorsellestir(ozellikler_df):
    
    plt.figure(figsize=(10, 6))
    sns.histplot(ozellikler_df['Derece Merkeziliği'], kde=True, color='blue', bins=20) 
    plt.title('Derece Merkeziliği Dağılımı')
    plt.xlabel('Derece Merkeziliği')
    plt.ylabel('Frekans')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(ozellikler_df['Arasındalık Merkeziliği'], kde=True, color='green', bins=20)
    plt.title('Arasındalık Merkeziliği Dağılımı')
    plt.xlabel('Betweenness Merkeziliği')
    plt.ylabel('Frekans')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(ozellikler_df['Yakınlık Merkeziliği'], kde=True, color='red', bins=20)
    plt.title('Yakınlık Merkeziliği Dağılımı')
    plt.xlabel('Closeness Merkeziliği')
    plt.ylabel('Frekans')
    plt.show()


def topluluk_tespiti(G):
   
    topluluklar = community_louvain.best_partition(G, weight='weight')

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42) 
    cmap = plt.cm.jet  
  
    nx.draw_networkx_nodes(G, pos, node_size=500, cmap=cmap, 
                           node_color=list(topluluklar.values()), alpha=0.8)

    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='gray')

    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    plt.title("Topluluk Tespiti Görselleştirmesi")
    plt.show()
    return topluluklar


def dugum_dereceleri_grafik(G):

    dereceler = dict(G.degree(weight='weight'))

    derece_df = pd.DataFrame(dereceler.items(), columns=['Dugum', 'Derece'])
    derece_df = derece_df.sort_values(by='Derece', ascending=False)

    plt.figure(figsize=(15, 8))
    ax = sns.barplot(x='Derece', y='Dugum', data=derece_df, palette='viridis')
    plt.xlabel('Derece')
    plt.ylabel('Düğüm')
    plt.title('Düğüm Dereceleri')

    for p in ax.patches:
        ax.annotate(f'{p.get_width()}', 
                    (p.get_width() + 0.1, p.get_y() + p.get_height() / 2),
                    ha='center', va='center', fontsize=12, color='black')

    plt.show()

    return derece_df


def bagli_bilesen_ozellikleri(G):
    
    bagli_bilesenler = list(nx.connected_components(G))

    bagli_bilesen_ozellikleri = []
    
    for bilesen in bagli_bilesenler:
        
        subgraph = G.subgraph(bilesen)
        
        dugum_sayisi = len(subgraph.nodes())
        kenar_sayisi = len(subgraph.edges())
        
        bagli_bilesen_ozellikleri.append({
            'Bileşen Düğüm Sayısı': dugum_sayisi,
            'Bileşen Kenar Sayısı': kenar_sayisi,
            'Bileşen Yoğunluğu': 2 * kenar_sayisi / (dugum_sayisi * (dugum_sayisi - 1)) if dugum_sayisi > 1 else 0
        })
    
    print(f"Bağlı Bileşen Sayısı: {len(bagli_bilesenler)}")

    for i, ozellik in enumerate(bagli_bilesen_ozellikleri, 1):        
        for key, value in ozellik.items():
            print(f"  {key}: {value}")
    return bagli_bilesen_ozellikleri


def ortalama_yol_uzunlugu(G):
    
    try:
        
        yol_uzunluklari = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))
        
        yol_uzunluklari_listesi = []

        for kaynak in yol_uzunluklari.values():
            for hedef, uzunluk in kaynak.items():
                if hedef != kaynak:
                    yol_uzunluklari_listesi.append(uzunluk)
        
        ortalama_yol = sum(yol_uzunluklari_listesi) / len(yol_uzunluklari_listesi)
        print("ortalama yol:", ortalama_yol)
        return ortalama_yol

    except nx.NetworkXError:
        return None
    
    
def kenar_sayisi(G):
    
    kenar_sayısı = len(G.edges())
    print("Kenar Sayısı:", kenar_sayısı)
    return kenar_sayısı


def dugum_sayisi(G):
        
    dugum_sayısı = len(G.nodes())
    print("Düğüm Sayısı:", dugum_sayısı)
    return dugum_sayısı


def yoğunluk_hesaplama(G):

    N = len(G.nodes())
    E = len(G.edges())

    if N > 1:
        yoğunluk = 2 * E / (N * (N - 1))
        print("Ağın yoğunluğu:", yoğunluk)
    else:
        yoğunluk = 0  
        print("Ağın yoğunluğu:", yoğunluk)
        
    return yoğunluk


def hesapla_ag_cap(G):
    
    
    largest_cc = max(nx.connected_components(G), key=len)  # En büyük bağlı bileşeni bulur.
    subgraph = G.subgraph(largest_cc)  # Bu bileşene ait alt grafiği oluşturur.

    try:
        cap = nx.diameter(subgraph, weight='weight')  # Ağırlıklı çap hesaplar.
        print(f"Ağın çapı : {cap}")
        return cap
    except nx.NetworkXError:
        print("Grafik için çap hesaplanamadı. Muhtemelen grafik parçalı.")
        return None



dosya_yolu = '/mnt/c/Users/CASPER/OneDrive/Masaüstü/Valorant Veri Seti/valorant_games.csv'
if os.path.exists(dosya_yolu):
    
    print(f"Dosya bulundu: {dosya_yolu}")
    df = pd.read_csv(dosya_yolu)
    eksik_deger_kontrol = df.isnull().sum()
      
   
    ajan_harita_oynanma = oynanma_sayıları(df)
    
    
    G_ag_bilgileri = grafikler(df)
    
   
    ag_ozellikleri_df = ag_ozellikleri(G_ag_bilgileri)
    ag_ozelliklerini_gorsellestir(ag_ozellikleri_df)
    
    
    topluluk = topluluk_tespiti(G_ag_bilgileri)
    
    
   
    if 'G_ag_bilgileri' in locals():
        derece_df = dugum_dereceleri_grafik(G_ag_bilgileri)
        
    bağlı_bileşen_öz = bagli_bilesen_ozellikleri(G_ag_bilgileri)
    
    
    ortalama_yol = ortalama_yol_uzunlugu(G_ag_bilgileri)
    

    kenar_sayısı = kenar_sayisi(G_ag_bilgileri)
    

    dugum_sayısı = dugum_sayisi(G_ag_bilgileri)

    yoğunluk = yoğunluk_hesaplama(G_ag_bilgileri)

    cap = hesapla_ag_cap(G_ag_bilgileri)

else:
    print(f"Dosya bulunamadı: {dosya_yolu}")
    
    
    