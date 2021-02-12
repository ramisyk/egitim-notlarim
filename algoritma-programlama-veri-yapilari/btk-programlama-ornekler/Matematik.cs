using System;
using System.Collections.Generic;

namespace btk_programlama_ornekler
{
    class Matematik
    {
        public List<int> Seri {get; set;}
        public Matematik(params int[] sayilar)
        {
            Seri = new List<int>();
            foreach(var sayi in sayilar)
                ElemanEkle(sayi);
        }

        public void ElemanEkle(int sayi) 
        {
            Seri.Add(sayi);
        }
        public void ElemanEkle(int[] sayilar) 
        {
            Seri.AddRange(sayilar);
        }

        public void Yazdir()
        {
            Console.WriteLine();
            if(Seri != null)
                Seri.ForEach(s => Console.Write("{0,5} ", s));
            else
                Console.WriteLine("\aSeri boş!!!");
            Console.WriteLine();

        }

        public int EnBuyukDegeriGetir() 
        {
            int enBuyuk = int.MinValue;
            foreach(var sayi in Seri)
                enBuyuk = Math.Max(enBuyuk, sayi);
            return enBuyuk;
        }
        public int EnKucukDegeriGetir() 
        {
            int enKucuk = int.MaxValue;
            foreach(var sayi in Seri)
                enKucuk = Math.Min(enKucuk, sayi);
            return enKucuk;
        }
        public int Topla()
        {
            int toplam = 0;
            foreach(var sayi in Seri)
                toplam += sayi;
            return toplam;
        }
        public int TekSayilarinToplami()
        {
            int sonuc = 0;
            for (int i = 0; i < Seri.Count; i++)
            {
                if(Seri[i] % 2 == 1)
                    sonuc += Seri[i];
            }
            return sonuc;
        }
        public int CiftayilarinToplami()
        {
            int sonuc = 0;
            for (int i = 0; i < Seri.Count; i++)
            {
                if(Seri[i] % 2 == 0)
                    sonuc += Seri[i];
            }
            return sonuc;
        }
        public double Ortalama()
        {
            return (double)Topla() / Seri.Count;
        }
    }
}
