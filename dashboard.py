import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memasukkan data tabel
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

# Menampilkan Pai Chart Rata-rata penyewaan Sepeda berdasarkan Musim
# Mengambil data
avg_season = day_df.groupby('season')['cnt'].mean()
labels_season = ["Spring", "Summer", "Fall", "Winter"]

st.write("### Rata-rata Penyewaan Sepeda Berdasarkan Musim")
st.write(avg_season)

# Membuat plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.pie(avg_season, labels=labels_season, autopct='%1.1f%%', colors=('#FFF67E', '#BFEA7C', 'lightblue', '#416D19'))
ax.set_title('Average Bike Sharing Based on Season')

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Menampilkan Donut Chart Penyewa Sepeda
# Data total jumlah pengguna terdaftar dan tidak terdaftar
cnt_bikesharing = [day_df['registered'].sum(), day_df['casual'].sum()]
labels = ['Registered', 'Unregistered']  # Label untuk potongan pie chart

st.write("### Data Jumlah Penyewa Sepeda")
st.write(cnt_bikesharing)

# Plot donut chart
fig, ax = plt.subplots(figsize=(7, 5))
ax.pie(cnt_bikesharing, labels=labels, autopct='%1.1f%%', colors=('#BFEA7C', '#416D19'), wedgeprops=dict(width=0.4))

# Lingkaran dalam untuk membuat tampilan donut chart
centre_circle = plt.Circle((0,0),0.5,color='black', fc='white',linewidth=1.25)
fig.gca().add_artist(centre_circle)  # Menambahkan lingkaran dalam ke dalam plot

# Judul plot
plt.title('Bicycle Rentals User Percentage (Registered and Unregistered)')

# Tambahkan label jumlah total pengguna
total_users = sum(cnt_bikesharing)
plt.annotate('Total Users: {}'.format(total_users), xy=(0, 0), fontsize=10, ha='center')

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Menampilkan Bar Chart Rata rata penggunaan sepeda pada hari kerja
# Data rata-rata jumlah sewa sepeda berdasarkan jenis hari (hari libur atau hari kerja)
avg_workingday = day_df.groupby('workingday')['cnt'].mean()
labels_workingday = ["Holiday", "Workingday"]  # Label untuk sumbu x

st.write("### Rata-rata Penyewaan Sepeda pada Hari Kerja")
st.write(avg_workingday)

# Plot bar chart
fig, ax = plt.subplots(figsize=(10, 5))  # Mengatur ukuran plot
ax.bar(labels_workingday, avg_workingday, color=['#FFF67E'])  # Membuat bar chart
ax.set_title("Average Bike Rentals on Working Days")  # Menambahkan judul
ax.set_xlabel("Day Type")  # Menambahkan label pada sumbu x
ax.set_ylabel("Average Count")  # Menambahkan label pada sumbu y
ax.grid(True)  # Menambahkan grid pada plot

# Menampilkan plot di Streamlit
st.pyplot(fig)