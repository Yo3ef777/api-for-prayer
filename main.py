from fastapi import FastAPI
from typing import List, Dict


app = FastAPI()

# فرض کنید اطلاعات مداحی‌ها در یک دیکشنری ذخیره شده‌اند
# هر مداحی دارای نام خواننده، نام مداحی و مدت زمان است
# اطلاعات مداحی‌ها را در این دیکشنری تعریف کنید
mock_maddahi_data = [
    {
        "id": "1",
        "name": "نمیدانم",
        "singer": "علیمی",
        "duration": "10:41",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/10.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/1.mp3",
        # سایر مشخصات مداحی
    },
    {
        "id": "2",
        "name": " ",
        "singer": "علیمی",
        "duration": "5:50",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/10.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/2.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "3",
        "name": " ",
        "singer": "علیمی",
        "duration": "5:11",
                "img": 'https://yo3ef777.github.io/api-for-prayer/img/10.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/3.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "4",
        "name": " ",
        "singer": "علیمی",
        "duration": "8:09",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/10.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/4.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "5",
        "name": " ",
        "singer": "علیمی",
        "duration": "2:56",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/10.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/5.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "6",
        "name": "بریم نجف",
        "singer": "امیر کرمانشاهی",
        "duration": "4:08",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/2.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/6.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "7",
        "name": " ",
        "singer": "قلیچ خانی",
        "duration": "2:30",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/10.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/7.mp3",
        # سایر مشخصاتی

    },
    {
        'id': "8",
        "name": " ",
        "singer": "قلیچ خانی",
        "duration": "3:24",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/4.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/8.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "9",
        "name": " ",
        "singer": "قلیچ خانی",
        "duration": "3:30",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/4.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/9.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "10",
        "name": " ",
        "singer": "قلیچ خانی",
        "duration": "2:08",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/4.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/10.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "11",
        "name": " ",
        "singer": "قلیچ خانی",
        "duration": "3:32",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/4.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/11.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "12",
        "name": " ",
        "singer": "قلیچ خانی",
        "duration": "3:20",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/4.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/12.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "13",
        "name": " ",
        "singer": "هلالی",
        "duration": "5:32",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/12.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/13.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "14",
        "name": " ",
        "singer": "هلالی",
        "duration": "37:00",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/12.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/14.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "15",
        "name": " ",
        "singer": "هلالی",
        "duration": "4:38",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/12.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/15.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "16",
        "name": " ",
        "singer": "هلالی",
        "duration": "6:49",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/12.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/16.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "17",
        "name": " ",
        "singer": "هلالی",
        "duration": "2:20",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/12.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/17.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "18",
        "name": " ",
        "singer": "هلالی",
        "duration": "2:53",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/12.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/18.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "19",
        "name": "سلام حامیه زندگیم",
        "singer": "حسین خلجی",
        "duration": "3:01",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/9.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/19.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "20",
        "name": "بارون ببار از طاق آسمون",
        "singer": "جواد مقدم",
        "duration": "10:09",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/13.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/20.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "21",
        "name": " ",
        "singer": "محمد کریمی",
        "duration": "3:53",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/8.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/21.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "22",
        "name": " ",
        "singer": "محمد کریمی",
        "duration": "13:06",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/8.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/22.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "23",
        "name": " ",
        "singer": "محمد کریمی",
        "duration": "3:47",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/8.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/23.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "24",
        "name": " ",
        "singer": "محمد کریمی",
        "duration": "3:38",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/8.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/24.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "25",
        "name": " ",
        "singer": "محمد کریمی",
        "duration": "4:12",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/8.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/25.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "26",
        "name": " ",
        "singer": "محمد کریمی",
        "duration": "16:42",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/8.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/26.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "27",
        "name": "سلام من به حسین",
        "singer": "محمد کریمی",
        "duration": "6:35",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/8.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/27.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "28",
        "name": "باید قلبم برای تو حرم بشه",
        "singer": "مجید بنی فاطمه",
        "duration": "7:12",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/7.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/28.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "29",
        "name": "یا علی یا عظیم",
        "singer": "حاج مهدی رسولی",
        "duration": "3:30",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/6.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/29.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "30",
        "name": "عاشق حسینیم به ابلفضل",
        "singer": "میسم متی",
        "duration": "8:05",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/30.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "31",
        "name": " ",
        "singer": "جواد مقدم",
        "duration": "5:22",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/13.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/31.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "32",
        "name": " ",
        "singer": "جواد مقدم",
        "duration": "4:06",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/13.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/32.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "33",
        "name": " ",
        "singer": "جواد مقدم",
        "duration": "6:57",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/13.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/33.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "34",
        "name": " ",
        "singer": "جواد مقدم",
        "duration": "7:58",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/13.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/34.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "35",
        "name": " ",
        "singer": "جواد مقدم",
        "duration": "5:31",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/13.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/35.mp3",
        # سایر مشخصاتی

    },

    {
        "id": "36",
        "name": " ",
        "singer": "جواد مقدم",
        "duration": "5:40",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/13.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/36.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "37",
        "name": " ",
        "singer": "جواد مقدم",
        "duration": "7:23",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/13.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/37.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "38",
        "name": "عشق یعنی سینه زنم",
        "singer": "محمد حسین پویانفر",
        "duration": "5:36",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/1.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/38.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "39",
        "name": " ",
        "singer": "مختاری",
        "duration": "9:53",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/1.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/39.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "40",
        "name": " ",
        "singer": "مختاری",
        "duration": "34:07",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/11.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/40.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "41",
        "name": " ",
        "singer": "مختاری",
        "duration": "3:19",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/11.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/41.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "42",
        "name": "دنیا محل گذره",
        "singer": "محمد حسین پویانفر",
        "duration": "3:15",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/1.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/42.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "43",
        "name": "نمیشه باورم",
        "singer": "سید رضا نریمانی",
        "duration": "6:16",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/5.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/43.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "44",
        "name": " ",
        "singer": "سیب سرخی",
        "duration": "3:45",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/14.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/44.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "45",
        "name": " ",
        "singer": "سیب سرخی",
        "duration": "6:41",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/14.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/45.mp3",
        # سایر مشخصاتی

    },

    {
        "id": "46",
        "name": " ",
        "singer": "سیب سرخی",
        "duration": "14:33",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/14.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/46.mp3",
        # سایر مشخصاتی

    },
    {
        "id": "47",
        "name": " ",
        "singer": "سیب سرخی",
        "duration": "28:30",
        "img": 'https://yo3ef777.github.io/api-for-prayer/img/14.jpg',
        "audio": "https://yo3ef777.github.io/api-for-prayer/madahi/1/47.mp3",
        # سایر مشخصات مداحی
    },
]


@app.get("/maddahi")
def get_maddahi_list() -> List[Dict[str, str]]:
    """
    درخواست GET برای دریافت لیست مداحی‌ها با اطلاعات مربوطه
    """
    return mock_maddahi_data

# می‌توانید روت‌های دیگری برای جزئیات مداحی‌ها ایجاد کنید
# مثلاً برای دریافت اطلاعات یک مداحی خاص

# برای اجرای این API، از دستور زیر استفاده کنید:
# uvicorn main:app --reload
