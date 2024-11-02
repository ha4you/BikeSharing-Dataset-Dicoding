import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

day_df['date'] = pd.to_datetime(day_df['dteday'])
hour_df['date'] = pd.to_datetime(hour_df['dteday'])

st.sidebar.image("https://raw.githubusercontent.com/ha4you/BikeSharing-Dataset-Dicoding/master/dashboard/logo-bikesharing.png")
st.sidebar.header('Filters')

start_date = st.sidebar.date_input("Start Date", day_df['dteday'].min())
end_date = st.sidebar.date_input("End Date", day_df['dteday'].max())
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

filtered_data_hari = day_df[(day_df['date'] >= start_date) & (day_df['date'] <= end_date)]
filtered_data_jam = hour_df[(hour_df['date'] >= start_date) & (hour_df['date'] <= end_date)]

st.title('Dashboard Bike Sharing Dataset')

october_2011_data = day_df[(day_df['dteday'] >= '2011-10-01') & (day_df['dteday'] <= '2011-10-31')]

st.subheader('Distribusi Harian Peminjam Sepeda Terdaftar dan Tidak Terdaftar')
fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(october_2011_data['dteday'], october_2011_data['registered'], marker='o', label='Pelanggan Terdaftar', color='royalblue')
ax.plot(october_2011_data['dteday'], october_2011_data['casual'], marker='o', label='Pelanggan Tidak Terdaftar', color='coral')

ax.set_title('Distribusi Harian Peminjam Sepeda Terdaftar dan Tidak Terdaftar (Oktober 2011)', fontsize=16)
ax.set_xlabel('Tanggal', fontsize=14)
ax.set_ylabel('Jumlah Peminjam', fontsize=14)
ax.legend(loc='upper right')
ax.tick_params(axis='x', rotation=45)
ax.grid(True)

st.pyplot(fig)

total_registered = day_df['registered'].sum()
total_casual = day_df['casual'].sum()

st.subheader('Total Peminjam Sepeda: Terdaftar vs Tidak Terdaftar')
fig, ax = plt.subplots(figsize=(8, 6))
labels = ['Pelanggan Terdaftar', 'Pelanggan Tidak Terdaftar']
sizes = [total_registered, total_casual]
colors = ['skyblue', 'coral']
ax.bar(labels, sizes, color=colors)
ax.set_title('Total Peminjam Sepeda: Terdaftar vs Tidak Terdaftar', fontsize=16)
ax.set_xlabel('Kategori Pelanggan', fontsize=14)
ax.set_ylabel('Jumlah Peminjam', fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.7)

st.pyplot(fig)

fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85)
ax.axis('equal')
ax.set_title('Persentase Pelanggan Terdaftar vs Tidak Terdaftar', fontsize=16)

st.pyplot(fig)

st.caption('Copyright © Hedwig Adityas 2024')
