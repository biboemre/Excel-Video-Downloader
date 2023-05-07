# Python Excel Video Downloader

Bu Python kodu, 

pandas ve pytube kütüphanelerini kullanarak bir Excel dosyasında yer alan YouTube video URL'lerini okuyarak, her bir videoyu indirir ve video adına uygun bir JPEG dosyası olarak kaydeder. 

Kod, indirme işlemi sırasında yalnızca .mp4 dosya uzantılı videoları seçer ve en yüksek çözünürlükteki akışı indirir. İndirme sırasında, bir indirme ilerlemesi çubuğu da gösterilir. Video indirme işlemi tamamlandıktan sonra, program, verilen URL'ye karşılık gelen Excel dosyasındaki "Upload" sütunundaki resim bağlantısını kullanarak videoya uygun bir kapağı indirir. 

Kod, her bir video için ayrı ayrı işlem yapar ve hataların yanı sıra her bir işlemin başarı durumunu da ekrana basar.
