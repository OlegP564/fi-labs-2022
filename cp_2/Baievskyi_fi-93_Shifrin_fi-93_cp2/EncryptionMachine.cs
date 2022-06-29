using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace CP_2_SymCrypto
{
    internal class EncryptionMachine
    {
        readonly String PathForFileToStatistic;
        
        Double _IndexOfCoincidence;
        Double _InverseIndexOfCoincidence;
        Double _MathematicalExpectationOfIndexOfCoincidence;
        public Double IndexOfCoincidence
        {
            private set { _IndexOfCoincidence = value; }
            get { return _IndexOfCoincidence; }
        }
        public Double InverseIndexOfCoincidence
        {
            private set { _InverseIndexOfCoincidence = value; }
            get { return _InverseIndexOfCoincidence; }
        }
        public Double MathematicalExpectationOfIndexOfCoincidence
        {
            private set { _MathematicalExpectationOfIndexOfCoincidence = value; }
            get { return _MathematicalExpectationOfIndexOfCoincidence; }
        }


        readonly static Dictionary<String, Int32> Monograms = new()
        {
            { "а", 0 },
            { "б", 1 },
            { "в", 2 },
            { "г", 3 },
            { "д", 4 },
            { "е", 5 },
            { "ж", 6 },
            { "з", 7 },
            { "и", 8 },
            { "й", 9 },
            { "к", 10 },
            { "л", 11 },
            { "м", 12 },
            { "н", 13 },
            { "о", 14 },
            { "п", 15 },
            { "р", 16 },
            { "с", 17 },
            { "т", 18 },
            { "у", 19 },
            { "ф", 20 },
            { "х", 21 },
            { "ц", 22 },
            { "ч", 23 },
            { "ш", 24 },
            { "щ", 25 },
            { "ъ", 26 },
            { "ы", 27 },
            { "ь", 28 },
            { "э", 29 },
            { "ю", 30 },
            { "я", 31 },
        };
        public SortedDictionary<Double, String> MonogramStatistics;
        public SortedDictionary<Double, String> BigramStatistics;

        public EncryptionMachine()
        {
            this.PathForFileToStatistic = @"D:\Download\KPI\S6\Симметрическая криптография\Лабораторные\КП2\CP_2_SymCrypto\Files\ForStatistic.txt";
            var OText = File.ReadAllText(PathForFileToStatistic);

            MonogramStatistics = CountMonogram(OText, false);
            
            this.IndexOfCoincidence = GetIndexOfCoincidence(OText);
            this.InverseIndexOfCoincidence = 1d / Monograms.Count;
            this.MathematicalExpectationOfIndexOfCoincidence = GetMathematicalExpectation_Of_IndexOfCoincidence(OText);
            
            BigramStatistics = CountBigramOrdered(OText, false);
        }

        #region Mono- and bigrams statistics
        public string CheckText(string text, Boolean space = false)
        {
            if (new Regex(@"[а-еж-я ]").IsMatch(text))
            {
                text = text.ToLower();
                text = Regex.Replace(text, "ё", "е");
                text = Regex.Replace(text, @"[^а-еж-я ]", " ");
                text = Regex.Replace(text, @"\s+", space ? " " : "");
            }

            return text;
        }

        SortedDictionary<Double, String> CountMonogram(string text, Boolean space)
        {
            var open_text = CheckText(text, space);
            var dictionary = new SortedDictionary<String, Double>();

            for (int q = 0; q < open_text.Length; q++)
            {
                var monogram = open_text[q].ToString();

                if (monogram != " ")
                    dictionary[monogram] = dictionary.ContainsKey(monogram) ? ++dictionary[monogram] : 1;
            }

            var monograms = dictionary.Keys.ToArray();

            foreach (var monogram in monograms)
                dictionary[monogram] = dictionary[monogram] / open_text.Length;

            var Sorted_By_Value_Monogram_Dictionary = new SortedDictionary<Double, String>();

            foreach (var monogram in dictionary.Keys.ToArray())
            {
                if (!Sorted_By_Value_Monogram_Dictionary.ContainsKey(dictionary[monogram]))
                    Sorted_By_Value_Monogram_Dictionary.Add(dictionary[monogram], monogram);
                else
                {
                    bool switch_ = true;
                    Int32 q = 1;
                    while (switch_)
                    {
                        try
                        {
                            Sorted_By_Value_Monogram_Dictionary.Add(dictionary[monogram] + q++ * 1E-15, monogram);
                        }
                        catch (Exception)
                        {
                            continue;
                        }

                        switch_ = false;
                    }
                }
            }

            return Sorted_By_Value_Monogram_Dictionary;
        }

        SortedDictionary<Double, String> CountBigramOrdered(string text, bool space)
        {
            // привет = пр ри ив ве ет

            var open_text = CheckText(text, space);
            var dictionary = new SortedDictionary<String, Double>();

            for (int q = 0; q < open_text.Length - 1; q++)
            {
                var bigram = open_text.Substring(q, 2);
                dictionary[bigram] = dictionary.ContainsKey(bigram) ? ++dictionary[bigram] : 1;
            }

            var bigrams = dictionary.Keys.ToArray();
            Int32 bigrams_amount = open_text.Length - 1;

            foreach (var bigram in bigrams)
                dictionary[bigram] = dictionary[bigram] / bigrams_amount;

            var Sorted_By_Value_Bigram_Dictionary = new SortedDictionary<Double, String>();

            foreach (var monogram in dictionary.Keys.ToArray())
                if (!Sorted_By_Value_Bigram_Dictionary.ContainsKey(dictionary[monogram]))
                    Sorted_By_Value_Bigram_Dictionary.Add(dictionary[monogram], monogram);
                else
                {
                    bool switch_ = true;
                    Int32 q = 1;
                    while (switch_)
                    {
                        try
                        {
                            Sorted_By_Value_Bigram_Dictionary.Add(dictionary[monogram] + q++ * 1E-15, monogram);
                        }
                        catch (Exception)
                        {
                            continue;
                        }

                        switch_ = false;
                    }
                }

            return Sorted_By_Value_Bigram_Dictionary;
        }
        #endregion

        #region Index of coincidence and it's mathematical expectation
        public Double GetIndexOfCoincidence(String Text)
        {
            var current_letter_frequency = new Double[Monograms.Count];

            for (int q = 0; q < Text.Length; q++)
            {
                var temp_key = Monograms[Text.Substring(q, 1)];
                current_letter_frequency[temp_key]++;
            }

            var Index_Of_Coincidence = 0d;

            for (int q = 0; q < Monograms.Count; q++)
            {
                Index_Of_Coincidence += current_letter_frequency[q] * (current_letter_frequency[q] - 1d);
            }

            Index_Of_Coincidence /= (Text.Length * (Text.Length - 1d));


            return Index_Of_Coincidence;
        }

        public Double GetMathematicalExpectation_Of_IndexOfCoincidence(String Text)
        {
            var Propabilities_array = CountMonogram(Text, false).Keys.ToArray();

            var MathematicalExpectation_Of_Index_Of_Coincidence = 0d;

            for (int q = 0; q < Monograms.Count; q++)
                MathematicalExpectation_Of_Index_Of_Coincidence += Propabilities_array[q] * Propabilities_array[q];


            return MathematicalExpectation_Of_Index_Of_Coincidence;
        }

        #endregion

        #region Cesar Cipher
        public String EncryptByCaesarCipher(String OText, Int32 Key)
        {
            StringBuilder CText = new();

            for (Int32 q = 0; q < OText.Length; q++)
                CText.Append((Monogram)((Monograms[OText[q].ToString()] + Key) % 32));

            return CText.ToString();
        }

        public String DecryptByCaesarCipher(String CText, Int32 Key)
        {
            return EncryptByCaesarCipher(CText, 32 - Key);
        }

        public Int32 GetCaesarCipherKey(String CText)
        {
            var current_monogram_statistics = CountMonogram(CText, false);

            var possible_keys = new Dictionary<Int32, Int32>();

            for (Int32 q = 0; q < current_monogram_statistics.Count; q++)
            {
                var Letter_of_current_statistic = Monograms[current_monogram_statistics.ElementAt(q).Value];
                var Letter_from_statistic = Monograms[MonogramStatistics.ElementAt(q).Value];

                var index = (Letter_of_current_statistic - Letter_from_statistic + 32) % 32;

                possible_keys[index] = possible_keys.ContainsKey(index) ? ++possible_keys[index] : 1;
            }

            return possible_keys.Aggregate((max_value_element, current_value_element) =>
                                                                                        max_value_element.Value > current_value_element.Value ?
                                                                                        max_value_element :
                                                                                        current_value_element).Key;
        }

        #endregion

        #region Vigenere Cipher
        public String EncryptByVigenereCipher(String OText, String Key)
        {
            StringBuilder CText = new();

            for (Int32 q = 0; q < OText.Length; q++)
                CText.Append((Monogram)((Monograms[OText[q].ToString()] + Monograms[Key[q % Key.Length].ToString()]) % 32));

            return CText.ToString();
        }

        public String DecryptByVigenereCipher(String CText, String Key)
        {
            StringBuilder newKey = new();

            for (Int32 q = 0; q < Key.Length; q++)
            {
                var key_letter = (Monogram)((32 - Monograms[Key.Substring(q, 1)]) % 32);
                newKey.Append(key_letter);
            }
            
            return EncryptByVigenereCipher(CText, newKey.ToString());
        }

        public String GetVigenereCipherKey(String CText)
        {
            var possible_key = "";
            
            for (Int32 q = 2; q < (CText.Length < 40 ? CText.Length : 40); q++)
            {
                var temp_list = new List<string>();
                var currentIndexOfCoincidence = 0d;

                for (int t = 0; t < q; t++)
                {
                    var CText_Y_i = new StringBuilder();

                    for (int w = t; w < CText.Length; w += q)
                        CText_Y_i.Append(CText[w]);
                    
                    currentIndexOfCoincidence += GetIndexOfCoincidence(CText_Y_i.ToString());
                    
                    temp_list.Add(CText_Y_i.ToString());
                }

                if (Math.Abs((currentIndexOfCoincidence / q) - this._InverseIndexOfCoincidence) >
                    Math.Abs((currentIndexOfCoincidence / q) - this._IndexOfCoincidence))
                {
                    for (int r = 0; r < temp_list.Count; r++)
                        possible_key += ((Monogram)MFunction(temp_list[r])).ToString();

                    break;
                }
            }

            return possible_key;
        }

        private Double MFunction(String CText)
        {
            var N_list = new Double[32];
            var max_M_value = 0d;
            var possible_Key = 0d;

            for (int q = 0; q < CText.Length; q++)
                N_list[Monograms[CText.Substring(q, 1)]]++;
            
            for (int g = 0; g < 32; g++)
            {
                var current_M_value = 0d;

                for (int q = 0; q < N_list.Length; q++)
                {
                    var t = MonogramStatistics.FirstOrDefault(x => x.Value == ((Monogram)q).ToString()).Key;
                    var tt = N_list[(q + g) % 32];

                    current_M_value += tt * t;
                }

                if (current_M_value > max_M_value)
                {
                    max_M_value = current_M_value;
                    possible_Key = g;
                }
            }

            return possible_Key;
        }

        #endregion

    }
}
