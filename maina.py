from flask import Flask, request, jsonify

app = Flask(__name__)

# DATABASE ĐẦY ĐỦ - 80 XE TỪ 25 HÃNG
cars = [
    # TOYOTA (8 xe)
    {'id': 1, 'brand': 'Toyota', 'model': 'Vios', 'year': 2020, 'price': 420000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'Số sàn', 'color': 'Trắng'},
    {'id': 2, 'brand': 'Toyota', 'model': 'Corolla Altis', 'year': 2021, 'price': 720000000, 'fuel': 'Xăng',
     'engine': '1.8L', 'transmission': 'CVT', 'color': 'Đen'},
    {'id': 3, 'brand': 'Toyota', 'model': 'Camry', 'year': 2022, 'price': 1250000000, 'fuel': 'Xăng', 'engine': '2.5L',
     'transmission': 'CVT', 'color': 'Bạc'},
    {'id': 4, 'brand': 'Toyota', 'model': 'Fortuner', 'year': 2021, 'price': 1350000000, 'fuel': 'Dầu',
     'engine': '2.8L', 'transmission': 'Số tự động', 'color': 'Xám'},
    {'id': 5, 'brand': 'Toyota', 'model': 'Innova', 'year': 2020, 'price': 850000000, 'fuel': 'Xăng', 'engine': '2.0L',
     'transmission': 'Số tự động', 'color': 'Trắng'},
    {'id': 6, 'brand': 'Toyota', 'model': 'Land Cruiser', 'year': 2023, 'price': 4500000000, 'fuel': 'Xăng',
     'engine': '4.5L', 'transmission': 'Số tự động', 'color': 'Trắng'},
    {'id': 7, 'brand': 'Toyota', 'model': 'Hiace', 'year': 2019, 'price': 750000000, 'fuel': 'Dầu', 'engine': '2.8L',
     'transmission': 'Số sàn', 'color': 'Đen'},
    {'id': 8, 'brand': 'Toyota', 'model': 'Raize', 'year': 2022, 'price': 420000000, 'fuel': 'Xăng', 'engine': '1.0L',
     'transmission': 'CVT', 'color': 'Đỏ'},

    # HONDA (7 xe)
    {'id': 9, 'brand': 'Honda', 'model': 'City', 'year': 2021, 'price': 580000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'CVT', 'color': 'Trắng'},
    {'id': 10, 'brand': 'Honda', 'model': 'Civic', 'year': 2022, 'price': 820000000, 'fuel': 'Xăng', 'engine': '1.8L',
     'transmission': 'CVT', 'color': 'Đen'},
    {'id': 11, 'brand': 'Honda', 'model': 'CR-V', 'year': 2021, 'price': 980000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'CVT', 'color': 'Bạc'},
    {'id': 12, 'brand': 'Honda', 'model': 'Accord', 'year': 2020, 'price': 950000000, 'fuel': 'Xăng', 'engine': '2.4L',
     'transmission': 'CVT', 'color': 'Xám'},
    {'id': 13, 'brand': 'Honda', 'model': 'HR-V', 'year': 2022, 'price': 720000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'CVT', 'color': 'Trắng'},
    {'id': 14, 'brand': 'Honda', 'model': 'BR-V', 'year': 2021, 'price': 620000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'CVT', 'color': 'Đen'},
    {'id': 15, 'brand': 'Honda', 'model': 'Brio', 'year': 2020, 'price': 380000000, 'fuel': 'Xăng', 'engine': '1.2L',
     'transmission': 'Số sàn', 'color': 'Trắng'},

    # MERCEDES (6 xe)
    {'id': 16, 'brand': 'Mercedes', 'model': 'C300', 'year': 2022, 'price': 2500000000, 'fuel': 'Xăng',
     'engine': '2.0L', 'transmission': 'Số tự động', 'color': 'Đen'},
    {'id': 17, 'brand': 'Mercedes', 'model': 'E350', 'year': 2023, 'price': 3200000000, 'fuel': 'Xăng',
     'engine': '3.0L', 'transmission': 'Số tự động', 'color': 'Trắng'},
    {'id': 18, 'brand': 'Mercedes', 'model': 'GLC300', 'year': 2022, 'price': 2800000000, 'fuel': 'Xăng',
     'engine': '2.0L', 'transmission': 'Số tự động', 'color': 'Bạc'},
    {'id': 19, 'brand': 'Mercedes', 'model': 'S450', 'year': 2023, 'price': 4500000000, 'fuel': 'Xăng',
     'engine': '3.0L', 'transmission': 'Số tự động', 'color': 'Đen'},
    {'id': 20, 'brand': 'Mercedes', 'model': 'G63', 'year': 2024, 'price': 8500000000, 'fuel': 'Xăng', 'engine': '4.0L',
     'transmission': 'Số tự động', 'color': 'Đen'},
    {'id': 21, 'brand': 'Mercedes', 'model': 'C200', 'year': 2021, 'price': 2200000000, 'fuel': 'Xăng',
     'engine': '1.5L', 'transmission': 'Số tự động', 'color': 'Trắng'},

    # BMW (6 xe)
    {'id': 22, 'brand': 'BMW', 'model': '320i', 'year': 2021, 'price': 1800000000, 'fuel': 'Xăng', 'engine': '2.0L',
     'transmission': 'Số tự động', 'color': 'Trắng'},
    {'id': 23, 'brand': 'BMW', 'model': '520i', 'year': 2022, 'price': 2200000000, 'fuel': 'Xăng', 'engine': '2.0L',
     'transmission': 'Số tự động', 'color': 'Đen'},
    {'id': 24, 'brand': 'BMW', 'model': 'X5', 'year': 2023, 'price': 3500000000, 'fuel': 'Xăng', 'engine': '3.0L',
     'transmission': 'Số tự động', 'color': 'Xám'},
    {'id': 25, 'brand': 'BMW', 'model': 'X3', 'year': 2022, 'price': 2400000000, 'fuel': 'Xăng', 'engine': '2.0L',
     'transmission': 'Số tự động', 'color': 'Bạc'},
    {'id': 26, 'brand': 'BMW', 'model': '730Li', 'year': 2023, 'price': 3800000000, 'fuel': 'Xăng', 'engine': '3.0L',
     'transmission': 'Số tự động', 'color': 'Đen'},
    {'id': 27, 'brand': 'BMW', 'model': 'X1', 'year': 2021, 'price': 1600000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'Số tự động', 'color': 'Trắng'},

    # FORD (5 xe)
    {'id': 28, 'brand': 'Ford', 'model': 'Ranger', 'year': 2021, 'price': 680000000, 'fuel': 'Dầu', 'engine': '2.0L',
     'transmission': 'Số sàn', 'color': 'Trắng'},
    {'id': 29, 'brand': 'Ford', 'model': 'Everest', 'year': 2022, 'price': 1100000000, 'fuel': 'Dầu', 'engine': '2.0L',
     'transmission': 'Số tự động', 'color': 'Đen'},
    {'id': 30, 'brand': 'Ford', 'model': 'EcoSport', 'year': 2020, 'price': 520000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'Số tự động', 'color': 'Đỏ'},
    {'id': 31, 'brand': 'Ford', 'model': 'Explorer', 'year': 2023, 'price': 1300000000, 'fuel': 'Xăng',
     'engine': '2.3L', 'transmission': 'Số tự động', 'color': 'Xám'},
    {'id': 32, 'brand': 'Ford', 'model': 'Focus', 'year': 2019, 'price': 550000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'Số tự động', 'color': 'Bạc'},

    # HYUNDAI (5 xe)
    {'id': 33, 'brand': 'Hyundai', 'model': 'Accent', 'year': 2020, 'price': 380000000, 'fuel': 'Xăng',
     'engine': '1.4L', 'transmission': 'Số sàn', 'color': 'Trắng'},
    {'id': 34, 'brand': 'Hyundai', 'model': 'Elantra', 'year': 2021, 'price': 620000000, 'fuel': 'Xăng',
     'engine': '1.6L', 'transmission': 'CVT', 'color': 'Đen'},
    {'id': 35, 'brand': 'Hyundai', 'model': 'Tucson', 'year': 2022, 'price': 850000000, 'fuel': 'Xăng',
     'engine': '1.6L', 'transmission': 'Số tự động', 'color': 'Bạc'},
    {'id': 36, 'brand': 'Hyundai', 'model': 'Santa Fe', 'year': 2023, 'price': 1100000000, 'fuel': 'Xăng',
     'engine': '2.5L', 'transmission': 'Số tự động', 'color': 'Xám'},
    {'id': 37, 'brand': 'Hyundai', 'model': 'Grand i10', 'year': 2020, 'price': 320000000, 'fuel': 'Xăng',
     'engine': '1.2L', 'transmission': 'Số sàn', 'color': 'Trắng'},

    # KIA (5 xe)
    {'id': 38, 'brand': 'Kia', 'model': 'Cerato', 'year': 2021, 'price': 520000000, 'fuel': 'Xăng', 'engine': '1.6L',
     'transmission': 'Số sàn', 'color': 'Trắng'},
    {'id': 39, 'brand': 'Kia', 'model': 'Seltos', 'year': 2022, 'price': 680000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'CVT', 'color': 'Đen'},
    {'id': 40, 'brand': 'Kia', 'model': 'Sportage', 'year': 2023, 'price': 920000000, 'fuel': 'Xăng', 'engine': '1.6L',
     'transmission': 'Số tự động', 'color': 'Bạc'},
    {'id': 41, 'brand': 'Kia', 'model': 'Carnival', 'year': 2024, 'price': 1400000000, 'fuel': 'Dầu', 'engine': '2.2L',
     'transmission': 'Số tự động', 'color': 'Xám'},
    {'id': 42, 'brand': 'Kia', 'model': 'K3', 'year': 2020, 'price': 480000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'CVT', 'color': 'Đỏ'},

    # MAZDA (4 xe)
    {'id': 43, 'brand': 'Mazda', 'model': 'CX-5', 'year': 2022, 'price': 920000000, 'fuel': 'Xăng', 'engine': '2.0L',
     'transmission': 'Số tự động', 'color': 'Đỏ'},
    {'id': 44, 'brand': 'Mazda', 'model': 'CX-8', 'year': 2023, 'price': 1250000000, 'fuel': 'Xăng', 'engine': '2.5L',
     'transmission': 'Số tự động', 'color': 'Trắng'},
    {'id': 45, 'brand': 'Mazda', 'model': 'Mazda3', 'year': 2021, 'price': 650000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'CVT', 'color': 'Đen'},
    {'id': 46, 'brand': 'Mazda', 'model': 'Mazda6', 'year': 2020, 'price': 720000000, 'fuel': 'Xăng', 'engine': '2.0L',
     'transmission': 'CVT', 'color': 'Bạc'},

    # VINFAST (4 xe)
    {'id': 47, 'brand': 'VinFast', 'model': 'Lux A2.0', 'year': 2022, 'price': 1100000000, 'fuel': 'Xăng',
     'engine': '2.0L', 'transmission': 'Số tự động', 'color': 'Trắng'},
    {'id': 48, 'brand': 'VinFast', 'model': 'Fadil', 'year': 2021, 'price': 380000000, 'fuel': 'Xăng', 'engine': '1.4L',
     'transmission': 'Số sàn', 'color': 'Đen'},
    {'id': 49, 'brand': 'VinFast', 'model': 'VF e34', 'year': 2023, 'price': 690000000, 'fuel': 'Điện',
     'engine': 'Điện', 'transmission': 'Số tự động', 'color': 'Xám'},
    {'id': 50, 'brand': 'VinFast', 'model': 'VF 8', 'year': 2023, 'price': 1200000000, 'fuel': 'Điện', 'engine': 'Điện',
     'transmission': 'Số tự động', 'color': 'Đen'},

    # AUDI (3 xe)
    {'id': 51, 'brand': 'Audi', 'model': 'A4', 'year': 2022, 'price': 2800000000, 'fuel': 'Xăng', 'engine': '2.0L',
     'transmission': 'Số tự động', 'color': 'Đen'},
    {'id': 52, 'brand': 'Audi', 'model': 'Q5', 'year': 2023, 'price': 3200000000, 'fuel': 'Xăng', 'engine': '2.0L',
     'transmission': 'Số tự động', 'color': 'Trắng'},
    {'id': 53, 'brand': 'Audi', 'model': 'Q7', 'year': 2021, 'price': 3500000000, 'fuel': 'Xăng', 'engine': '3.0L',
     'transmission': 'Số tự động', 'color': 'Bạc'},

    # LEXUS (3 xe)
    {'id': 54, 'brand': 'Lexus', 'model': 'ES350', 'year': 2023, 'price': 3200000000, 'fuel': 'Xăng', 'engine': '3.5L',
     'transmission': 'Số tự động', 'color': 'Trắng'},
    {'id': 55, 'brand': 'Lexus', 'model': 'RX350', 'year': 2022, 'price': 3500000000, 'fuel': 'Xăng', 'engine': '3.5L',
     'transmission': 'Số tự động', 'color': 'Đen'},
    {'id': 56, 'brand': 'Lexus', 'model': 'NX350', 'year': 2023, 'price': 2800000000, 'fuel': 'Xăng', 'engine': '2.5L',
     'transmission': 'Số tự động', 'color': 'Xám'},

    # PORSCHE (2 xe)
    {'id': 57, 'brand': 'Porsche', 'model': 'Cayenne', 'year': 2023, 'price': 5500000000, 'fuel': 'Xăng',
     'engine': '3.0L', 'transmission': 'Số tự động', 'color': 'Đen'},
    {'id': 58, 'brand': 'Porsche', 'model': 'Macan', 'year': 2022, 'price': 3200000000, 'fuel': 'Xăng',
     'engine': '2.0L', 'transmission': 'Số tự động', 'color': 'Trắng'},

    # CHEVROLET (2 xe)
    {'id': 59, 'brand': 'Chevrolet', 'model': 'Spark', 'year': 2021, 'price': 320000000, 'fuel': 'Xăng',
     'engine': '1.2L', 'transmission': 'Số sàn', 'color': 'Trắng'},
    {'id': 60, 'brand': 'Chevrolet', 'model': 'Trailblazer', 'year': 2023, 'price': 850000000, 'fuel': 'Xăng',
     'engine': '1.3L', 'transmission': 'CVT', 'color': 'Đen'},

    # MITSUBISHI (2 xe)
    {'id': 61, 'brand': 'Mitsubishi', 'model': 'Xpander', 'year': 2022, 'price': 620000000, 'fuel': 'Xăng',
     'engine': '1.5L', 'transmission': 'CVT', 'color': 'Bạc'},
    {'id': 62, 'brand': 'Mitsubishi', 'model': 'Outlander', 'year': 2021, 'price': 780000000, 'fuel': 'Xăng',
     'engine': '2.4L', 'transmission': 'CVT', 'color': 'Xám'},

    # SUZUKI (2 xe)
    {'id': 63, 'brand': 'Suzuki', 'model': 'Ertiga', 'year': 2020, 'price': 420000000, 'fuel': 'Xăng', 'engine': '1.5L',
     'transmission': 'Số sàn', 'color': 'Trắng'},
    {'id': 64, 'brand': 'Suzuki', 'model': 'Swift', 'year': 2022, 'price': 520000000, 'fuel': 'Xăng', 'engine': '1.2L',
     'transmission': 'CVT', 'color': 'Đỏ'},

    # NISSAN (2 xe)
    {'id': 65, 'brand': 'Nissan', 'model': 'Sunny', 'year': 2019, 'price': 380000000, 'fuel': 'Xăng', 'engine': '1.6L',
     'transmission': 'CVT', 'color': 'Bạc'},
    {'id': 66, 'brand': 'Nissan', 'model': 'X-Trail', 'year': 2021, 'price': 850000000, 'fuel': 'Xăng',
     'engine': '2.5L', 'transmission': 'CVT', 'color': 'Đen'},

    # VOLVO (2 xe)
    {'id': 67, 'brand': 'Volvo', 'model': 'XC60', 'year': 2022, 'price': 2800000000, 'fuel': 'Xăng', 'engine': '2.0L',
     'transmission': 'Số tự động', 'color': 'Trắng'},
    {'id': 68, 'brand': 'Volvo', 'model': 'XC90', 'year': 2023, 'price': 3500000000, 'fuel': 'Xăng', 'engine': '2.0L',
     'transmission': 'Số tự động', 'color': 'Đen'},

    # LAND ROVER (2 xe)
    {'id': 69, 'brand': 'Land Rover', 'model': 'Range Rover Evoque', 'year': 2021, 'price': 3200000000, 'fuel': 'Xăng',
     'engine': '2.0L', 'transmission': 'Số tự động', 'color': 'Xám'},
    {'id': 70, 'brand': 'Land Rover', 'model': 'Discovery Sport', 'year': 2022, 'price': 2800000000, 'fuel': 'Dầu',
     'engine': '2.0L', 'transmission': 'Số tự động', 'color': 'Bạc'},

    # JEEP (2 xe)
    {'id': 71, 'brand': 'Jeep', 'model': 'Wrangler', 'year': 2020, 'price': 2500000000, 'fuel': 'Xăng',
     'engine': '2.4L', 'transmission': 'Số tự động', 'color': 'Đỏ'},
    {'id': 72, 'brand': 'Jeep', 'model': 'Grand Cherokee', 'year': 2021, 'price': 3200000000, 'fuel': 'Xăng',
     'engine': '3.6L', 'transmission': 'Số tự động', 'color': 'Trắng'},

    # SUBARU (2 xe)
    {'id': 73, 'brand': 'Subaru', 'model': 'Forester', 'year': 2022, 'price': 3500000000, 'fuel': 'Xăng',
     'engine': '2.0L', 'transmission': 'Số tự động', 'color': 'Bạc'},
    {'id': 74, 'brand': 'Subaru', 'model': 'Outback', 'year': 2023, 'price': 4200000000, 'fuel': 'Xăng',
     'engine': '2.0L', 'transmission': 'Số tự động', 'color': 'Xám'},

    # MASERATI (2 xe)
    {'id': 75, 'brand': 'Maserati', 'model': 'Ghibli', 'year': 2021, 'price': 8500000000, 'fuel': 'Xăng',
     'engine': '3.0L', 'transmission': 'Số tự động', 'color': 'Đen'},
    {'id': 76, 'brand': 'Maserati', 'model': 'Levante', 'year': 2022, 'price': 12000000000, 'fuel': 'Xăng',
     'engine': '3.8L', 'transmission': 'Số tự động', 'color': 'Trắng'},

    # BENTLEY (2 xe)
    {'id': 77, 'brand': 'Bentley', 'model': 'Continental GT', 'year': 2023, 'price': 25000000000, 'fuel': 'Xăng',
     'engine': '4.0L', 'transmission': 'Số tự động', 'color': 'Đỏ'},
    {'id': 78, 'brand': 'Bentley', 'model': 'Bentayga', 'year': 2024, 'price': 35000000000, 'fuel': 'Xăng',
     'engine': '6.0L', 'transmission': 'Số tự động', 'color': 'Vàng'},

    # ROLLS ROYCE (2 xe)
    {'id': 79, 'brand': 'Rolls Royce', 'model': 'Ghost', 'year': 2022, 'price': 35000000000, 'fuel': 'Xăng',
     'engine': '6.6L', 'transmission': 'Số tự động', 'color': 'Bạc'},
    {'id': 80, 'brand': 'Rolls Royce', 'model': 'Phantom', 'year': 2023, 'price': 45000000000, 'fuel': 'Xăng',
     'engine': '6.7L', 'transmission': 'Số tự động', 'color': 'Đen'},

    # FERRARI (2 xe)
    {'id': 81, 'brand': 'Ferrari', 'model': 'Portofino', 'year': 2023, 'price': 35000000000, 'fuel': 'Xăng',
     'engine': '3.9L', 'transmission': 'Số tự động', 'color': 'Đỏ'},
    {'id': 82, 'brand': 'Ferrari', 'model': 'Roma', 'year': 2024, 'price': 45000000000, 'fuel': 'Xăng',
     'engine': '4.0L', 'transmission': 'Số tự động', 'color': 'Vàng'},

    # LAMBORGHINI (2 xe)
    {'id': 83, 'brand': 'Lamborghini', 'model': 'Huracan', 'year': 2022, 'price': 45000000000, 'fuel': 'Xăng',
     'engine': '5.2L', 'transmission': 'Số tự động', 'color': 'Bạc'},
    {'id': 84, 'brand': 'Lamborghini', 'model': 'Urus', 'year': 2023, 'price': 52000000000, 'fuel': 'Xăng',
     'engine': '4.0L', 'transmission': 'Số tự động', 'color': 'Đen'}
]


@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hệ Thống Tra Cứu Xe Hơi Đầy Đủ</title>
        <meta charset="UTF-8">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
                color: #333;
            }
            .container {
                max-width: 1400px;
                margin: 0 auto;
            }
            .header {
                text-align: center;
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                margin-bottom: 30px;
            }
            .car-icon {
                font-size: 60px;
                margin-bottom: 15px;
            }
            h1 {
                color: #333;
                font-size: 36px;
                margin-bottom: 10px;
            }
            .subtitle {
                color: #666;
                font-size: 18px;
                margin-bottom: 15px;
            }
            .features {
                display: flex;
                justify-content: center;
                gap: 10px;
                flex-wrap: wrap;
                margin-top: 15px;
            }
            .feature-tag {
                background: #007bff;
                color: white;
                padding: 5px 12px;
                border-radius: 15px;
                font-size: 12px;
                font-weight: 600;
            }
            .main-content {
                display: grid;
                grid-template-columns: 320px 1fr;
                gap: 30px;
            }
            .filters-section {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                height: fit-content;
            }
            .results-section {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            .section-title {
                color: #333;
                margin-bottom: 20px;
                font-size: 24px;
                border-bottom: 3px solid #007bff;
                padding-bottom: 10px;
            }
            .form-group {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 8px;
                font-weight: 600;
                color: #555;
                font-size: 14px;
            }
            input, select {
                width: 100%;
                padding: 12px 15px;
                border: 2px solid #e1e5e9;
                border-radius: 8px;
                font-size: 16px;
                transition: all 0.3s ease;
                background: #f8f9fa;
            }
            input:focus, select:focus {
                border-color: #007bff;
                background: white;
                outline: none;
                box-shadow: 0 0 0 3px rgba(0,123,255,0.1);
            }
            button {
                background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
                color: white;
                padding: 15px 25px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
                font-weight: 600;
                transition: all 0.3s ease;
                width: 100%;
            }
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0,123,255,0.3);
            }
            .stats {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 15px;
                margin-bottom: 25px;
            }
            .stat-item {
                text-align: center;
                padding: 15px;
                background: #f8f9fa;
                border-radius: 8px;
            }
            .stat-value {
                font-size: 20px;
                font-weight: bold;
                color: #007bff;
            }
            .stat-label {
                font-size: 12px;
                color: #666;
                margin-top: 5px;
            }
            .search-results {
                margin-top: 20px;
            }
            .results-count {
                margin-bottom: 15px;
                font-weight: 600;
                color: #555;
                font-size: 16px;
            }
            .car-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
                gap: 20px;
            }
            .car-card {
                border: 1px solid #e1e5e9;
                border-radius: 10px;
                padding: 20px;
                background: #f8f9fa;
                transition: all 0.3s ease;
            }
            .car-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            }
            .car-header {
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
                margin-bottom: 15px;
            }
            .car-brand {
                font-size: 18px;
                font-weight: bold;
                color: #333;
            }
            .car-year {
                background: #007bff;
                color: white;
                padding: 4px 8px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: bold;
            }
            .car-model {
                font-size: 16px;
                color: #666;
                margin-bottom: 10px;
            }
            .car-price {
                font-size: 20px;
                font-weight: bold;
                color: #28a745;
                margin-bottom: 15px;
            }
            .car-details {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 10px;
                font-size: 14px;
                margin-bottom: 10px;
            }
            .car-detail {
                display: flex;
                align-items: center;
                gap: 5px;
            }
            .car-color {
                padding-top: 10px;
                border-top: 1px solid #e1e5e9;
                font-size: 13px;
                color: #666;
            }
            .luxury-badge {
                background: #ffc107;
                color: #212529;
                padding: 2px 8px;
                border-radius: 10px;
                font-size: 10px;
                font-weight: bold;
                margin-left: 5px;
            }
            .supercar-badge {
                background: #dc3545;
                color: white;
                padding: 2px 8px;
                border-radius: 10px;
                font-size: 10px;
                font-weight: bold;
                margin-left: 5px;
            }
            .loading {
                display: inline-block;
                width: 20px;
                height: 20px;
                border: 3px solid #ffffff;
                border-radius: 50%;
                border-top-color: transparent;
                animation: spin 1s ease-in-out infinite;
                margin-right: 10px;
            }
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            @media (max-width: 768px) {
                .main-content {
                    grid-template-columns: 1fr;
                }
                .stats {
                    grid-template-columns: 1fr 1fr;
                }
                .car-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="car-icon">🚗</div>
                <h1>HỆ THỐNG TRA CỨU XE HƠI ĐẦY ĐỦ</h1>
                <p class="subtitle">Database 84 mẫu xe từ 25 hãng xe - Tìm kiếm thông tin chi tiết</p>
                <div class="features">
                    <div class="feature-tag">🚗 25 Hãng xe</div>
                    <div class="feature-tag">📊 84 Mẫu xe</div>
                    <div class="feature-tag">💰 Đa dạng giá</div>
                    <div class="feature-tag">⚡ Tìm kiếm thông minh</div>
                </div>
            </div>

            <div class="main-content">
                <div class="filters-section">
                    <h2 class="section-title">🔍 TÌM KIẾM</h2>

                    <div class="form-group">
                        <label for="brand">Hãng xe:</label>
                        <select id="brand">
                            <option value="">Tất cả hãng xe</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="model">Dòng xe:</label>
                        <input type="text" id="model" placeholder="Nhập tên dòng xe...">
                    </div>

                    <div class="form-group">
                        <label for="min_year">Năm sản xuất từ:</label>
                        <input type="number" id="min_year" min="2000" max="2024" value="2018">
                    </div>

                    <div class="form-group">
                        <label for="max_year">Đến năm:</label>
                        <input type="number" id="max_year" min="2000" max="2024" value="2024">
                    </div>

                    <div class="form-group">
                        <label for="fuel_type">Loại nhiên liệu:</label>
                        <select id="fuel_type">
                            <option value="">Tất cả</option>
                            <option value="Xăng">Xăng</option>
                            <option value="Dầu">Dầu</option>
                            <option value="Điện">Điện</option>
                        </select>
                    </div>

                    <button onclick="searchCars()" id="searchBtn">
                        🔍 TÌM KIẾM
                    </button>
                </div>

                <div class="results-section">
                    <h2 class="section-title">📊 KẾT QUẢ TRA CỨU</h2>

                    <div class="stats" id="systemStats">
                        <div class="stat-item">
                            <div class="stat-value" id="totalCars">84</div>
                            <div class="stat-label">TỔNG SỐ XE</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-value" id="totalBrands">25</div>
                            <div class="stat-label">HÃNG XE</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-value" id="totalModels">84</div>
                            <div class="stat-label">MẪU XE</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-value" id="avgPrice">-</div>
                            <div class="stat-label">GIÁ TRUNG BÌNH</div>
                        </div>
                    </div>

                    <div class="search-results">
                        <div class="results-count" id="resultsCount">
                            Tìm thấy 84 xe
                        </div>

                        <div class="car-grid" id="carResults">
                            <!-- Kết quả sẽ hiển thị ở đây -->
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script>
            const allCars = ''' + str(cars) + ''';

            // Load khi trang web tải xong
            document.addEventListener('DOMContentLoaded', function() {
                loadBrands();
                loadSystemStats();
                displayCars(allCars);
            });

            // Load danh sách hãng xe
            function loadBrands() {
                const brands = [...new Set(allCars.map(car => car.brand))].sort();
                const brandSelect = document.getElementById('brand');
                brandSelect.innerHTML = '<option value="">Tất cả hãng xe</option>';

                brands.forEach(brand => {
                    const option = document.createElement('option');
                    option.value = brand;
                    option.textContent = brand;
                    brandSelect.appendChild(option);
                });
            }

            // Load thống kê hệ thống
            function loadSystemStats() {
                const totalPrice = allCars.reduce((sum, car) => sum + car.price, 0);
                const avgPrice = (totalPrice / allCars.length).toLocaleString();
                document.getElementById('avgPrice').textContent = avgPrice + ' VND';
            }

            function displayCars(carList) {
                const resultsDiv = document.getElementById('carResults');
                const countDiv = document.getElementById('resultsCount');

                countDiv.textContent = `Tìm thấy ${carList.length} xe`;
                resultsDiv.innerHTML = carList.map(car => {
                    let badge = '';
                    if (car.price > 10000000000) {
                        badge = '<span class="supercar-badge">SIÊU XE</span>';
                    } else if (car.price > 3000000000) {
                        badge = '<span class="luxury-badge">CAO CẤP</span>';
                    }

                    return `
                        <div class="car-card">
                            <div class="car-header">
                                <div class="car-brand">${car.brand} ${badge}</div>
                                <div class="car-year">${car.year}</div>
                            </div>
                            <div class="car-model">${car.model}</div>
                            <div class="car-price">${car.price.toLocaleString()} VND</div>
                            <div class="car-details">
                                <div class="car-detail">⚙️ ${car.engine}</div>
                                <div class="car-detail">⛽ ${car.fuel}</div>
                                <div class="car-detail">🔧 ${car.transmission}</div>
                                <div class="car-detail">🎨 ${car.color}</div>
                            </div>
                        </div>
                    `;
                }).join('');
            }

            function searchCars() {
                const brand = document.getElementById('brand').value;
                const model = document.getElementById('model').value.toLowerCase();
                const fuelType = document.getElementById('fuel_type').value;
                const minYear = parseInt(document.getElementById('min_year').value);
                const maxYear = parseInt(document.getElementById('max_year').value);

                const filteredCars = allCars.filter(car => {
                    let match = true;

                    if (brand && car.brand !== brand) match = false;
                    if (model && !car.model.toLowerCase().includes(model)) match = false;
                    if (fuelType && car.fuel !== fuelType) match = false;
                    if (car.year < minYear || car.year > maxYear) match = false;

                    return match;
                });

                displayCars(filteredCars);
            }
        </script>
    </body>
    </html>
    '''


if __name__ == '__main__':
    print("🚗 KHỞI ĐỘNG HỆ THỐNG TRA CỨU XE HƠI ĐẦY ĐỦ")
    print(f"📊 Tổng số xe: {len(cars)}")
    print(f"🏷️ Số hãng xe: {len(set(car['brand'] for car in cars))}")
    total_price = sum(car['price'] for car in cars)
    print(f"💰 Giá trung bình: {total_price / len(cars):,.0f} VND")
    print(f"📈 Giá cao nhất: {max(car['price'] for car in cars):,.0f} VND")
    print(f"📉 Giá thấp nhất: {min(car['price'] for car in cars):,.0f} VND")
    print("🌐 Truy cập: http://localhost:5000")
    app.run(debug=True, port=5000)