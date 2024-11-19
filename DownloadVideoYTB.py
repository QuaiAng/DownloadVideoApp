#Thêm các thư viện cần thiết
import tkinter as tk
from pytube import YouTube
import os
from tkinter import messagebox
import re

#Hàm dùng để kiểm tra xem một link có phải là link Youtube hay không, nếu đúng trả về True,
#ngược lại trả về False
def is_Youtube_link(link):

    #Định dạng của link Youtube
    youtube_link_regex = (
        r'(https?://)?(www.)?'
        '(youtube|youtu|youtube-nocookie).(com|be)/'
        '(watch?v=|embed/|v/|.+?v=)?([^&=%?]{11})'
    )
    
    youtube_link_regex_match = re.match(youtube_link_regex, link)

    if youtube_link_regex_match:
        return True 
    else:
        return False  

#Hàm dùng để tải video
def download_video():

    #Lấy ra link từ giá trị của Entry (Do người dùng nhập)
    link = link_text.get()

    #Kiểm tra xem link đó có phải là một link Youtube không
    if not is_Youtube_link(link):
        messagebox.showerror("Lỗi", "Link bạn cung cấp không phải là một link Youtube, vui lòng kiểm tra lại !")
        return

    yt = YouTube(link)
    
    #Lọc ra file có đuôi .mp4 và lấy file có chất lượng cao nhất
    video = yt.streams.filter(file_extension='mp4').get_highest_resolution()

    #Tạo đường dẫn lưu video
    download_folder = "D:/Video Download"

    # Kiểm tra nếu thư mục chưa tồn tại thì tạo mới
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    video.download(download_folder)

    messagebox.showinfo("Thành Công", "Video đã được tải xuống tại " + download_folder)


window = tk.Tk()
window.title('Download YouTube Video')

#Tạo ra label để mô tả cho người dùng biết nên điền link vào
link_label = tk.Label(window, text="Link Video YouTube:")
link_label.pack(pady=5)

#Tạo ra Entry để chứa link video
link_text = tk.Entry(window, width=50)
link_text.pack(pady=5)

#Tạo ra nút để khi ấn vào thì kích hoạt hàm tải video về
download_button = tk.Button(window, text="Tải Video", command=download_video)
download_button.pack(pady=20)

window.mainloop()