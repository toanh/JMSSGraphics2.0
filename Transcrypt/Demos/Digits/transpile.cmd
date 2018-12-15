copy /Y ..\..\JMSSGraphics.py
copy /Y ..\..\JMSSNeural.py
python -m transcrypt -b -m -n Digits.py
python -m http.server