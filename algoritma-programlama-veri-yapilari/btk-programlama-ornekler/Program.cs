using System;
using System.Collections.Generic;

namespace btk_programlama_ornekler
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] sayilar = {23, 57, 42};
            Matematik mat = new Matematik(3, 5, 7, 10);
            mat.ElemanEkle(5);
            mat.ElemanEkle(15);
            mat.ElemanEkle(sayilar);
            mat.Yazdir();
            Console.WriteLine("Dizinin en büyük elemanı : {0}", mat.EnBuyukDegeriGetir().ToString());
            Console.WriteLine("Dizinin en küçük elemanı : {0}", mat.EnKucukDegeriGetir().ToString());
            Console.WriteLine("Dizideki elemanların toplamı : {0}", mat.Topla().ToString());
            Console.WriteLine("Dizideki tek sayıların toplamı : {0}", mat.TekSayilarinToplami().ToString());
            Console.WriteLine("Dizideki çift sayıların toplamı : {0}", mat.CiftayilarinToplami().ToString());
            Console.WriteLine("Dizideki elemanların ortalaması : {0:N1}", mat.Ortalama());
        }
    }
}
