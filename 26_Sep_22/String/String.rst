====================
Mutuable & Immutable
====================
* python တွင် variable တိုင်းမှာ object တစ်ခုစီ၏ instance ဆိုတာရှိတယ်။ 
* python မှာ *Mutable object* နှင့်  *Immutable object* ဆိုပြီး နှစ်မျိုးရှိသည်။
* Object တစ်ခုကို instantiate လုပ်တဲ့အခါတိုင်း၊ a unique object idတစ်ခု သတ်မှတ်ပေးပါတယ်။
* Object ရဲ့ typeကို runtime တွင် definedသတ်မှတ်ထားပြီးနောက်မှ အဲ့ဒါကိုပြောင်းလို့ မရပါ။ ဒါပေမဲ့ အဲ့ဒီအခြေအနေကို ပြောင်းလဲနိုင်တယ်ဆိုရင် အဲ့ဒါကို mutable objectလို့ခေါ်တယ်။
* *Mutable object များသည် သူတို့ရဲ့ state သို့ contentsတွေကို ပြောင်းလဲနိုင်ပြီး *Immutable object* များသည် သူတို့ရဲ့ state သို့ contentကို ပြောင်းလဲလို့ မရပါ။
* *Immutable Objects* : 
     * built-in types like *int, float, bool, string, unicode, tuple*.
     * အရိုးရှင်းဆုံးပြောရမယ်ဆိုရင်၊ Immutable Objectတစ်ခုကို createdလုပ်ပြီးရင် ပြောင်းလဲလို့မရပါဘူး။
* *Mutable Objects* : 
     * *list, dict, set* . Custom classesတွေဟာ generallyအားဖြင့် mutableပြောင်းလဲနိုင်ပါတယ်။ 
* .. Note::
     We know that tuple in python is immutable. But, the tuple consists of a sequence of names with unchangeable bindings to objects.
* ::
    tup1 = ('apple', 'banana',[5,4,3,2,1])
  
    tup2 = ('apple', 'banana',[5,4,3,2,1])

* ဒီ tuple မှာဆိုရင် string နှင့် list တစ်ခု ပါဝင်ပါသည်။ Stringsတွေက immutable ကဖြစ်သောကြောင့် can’t change its value သူရဲ့ value ကို မပြောင်းလဲနိုင်ပါဘူး။ ဒါပေမယ့် list ထဲမှာပါတဲ့ contents တွေက ပြောင်းလဲနိုင်ပါတယ်။ Tuple သည် သူကိုယ်တိုင်က မပြောင်းလဲနိုင်သော်လည်း ပြောင်းလဲနိုင်သော အရာများပါရှိတယ်။
* ::
    print(tup1==tup2) ***#Output is True***

    print(tup1 is tup2) ***#Output is False***

    tup1[2].append(90)

    print(tup1) ***#Output is ('apple', 'banana', [5, 4, 3, 2, 1, 90])***
    
    print(tup1==tup2) ***#Output is False***