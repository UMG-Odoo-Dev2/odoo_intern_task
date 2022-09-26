# Trivial Compress and Decompress
    a = ""
    print("Original is {} bytes".format(getsizeof(original)))
Variable တစ်ခုရဲ့ original size က 49 byte ရှိတယ် Variable ထဲမှာ ကျွန်တော်တို့ data တစ်လုံးထည့် မယ်ဆိုရင် +1 byte တိုးသွာတယ်

    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))

compress ရဲ့  minimun က 28 bytes ရှိတယ် နောက်ထပ် ထပ်တိုးမယ်ဆိုရင် 4 bytes ထပ်တိုးတယ် ဘာလို့ 4 byte ထပ်တိုးသလဲ ဆိုရင် 4 bytes ဆိုရင် 32 bit ရှိတယ် Python 3.8.10 version က system 32 ကို support ပေးထားလို့ ကျွန်တော်ထင်တယ် 

