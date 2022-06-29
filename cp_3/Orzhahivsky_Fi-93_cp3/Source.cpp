#include <iostream>;
#include <string>;
#include "windows.h";
#include <fstream>;
#include <iomanip> 

using namespace std;
const int M = 31;
const int MB = 10;
const int A26 = 28;
const int A27 = 27;

string readFile(string Name)
{
    ifstream fin(Name);
    string res;
    if (fin.is_open())
    {
        string line = "";
        while (getline(fin, line))
        {
            string temp = "";
            for (int i = 0; i < size(line); i++)
            {
                int ch = line[i];
                ch += 32;
                if (ch == -40 || ch == -56)
                {
                    ch = 5;
                }
                if (ch < 0)
                {
                    ch += 32;
                }
                if (ch >= 0 && ch < 32)
                {
                    if (ch == 26)
                    {
                        ch = 28;
                    }
                    temp += (char)(ch - 32);
                }
            }
            res += temp;
        }
    }
    fin.close();
    return res;
}
int turnedEl(int a, int n)
{
    if (a < 0)
        a *= -1;
    int s1 = 1, s2 = 0;
    int t1 = 0, t2 = 1;
    int m = n;
    while (n != 0)
    {
        int q = a / n;
        int r = a % n;
        a = n;
        n = r;
        int tempS = s1 - s2 * q;
        s1 = s2;
        s2 = tempS;
        int tempR = t1 - t2 * q;
        t1 = t2;
        t2 = tempR;
    }
    if (s1 < 0)
    {
        s1 = s1 + m;
    }
    return s1;
}
void bigrams(string Text, double(&arr)[M][M])
{
    int check = 0;
    int first = -1;
    int second = -1;
    int m = M;
    int n = 0;
    for (int i = 0; i < size(Text); i++)
    {
        int temp = (int)Text[i];
        temp += 32;
        if (temp == -40 || temp == -56)
        {
            temp == 5;
        }
        if (temp >= -32 && temp < 0)
        {
            temp += 32;
        }
        if (temp == 27)
        {
            if (A26 == 27)
            {
                temp = 26;
            }
        }
        if (temp == 28)
        {
            if (A27 == 28)
            {
                temp = 27;
            }
            else
            {
                temp = 26;
            }
        }
        if (temp > 28)
        {
            temp--;
        }
        if (temp >= 0 && temp < 32 && check == 0)
        {

            first = temp;
            check++;
        }
        else if (temp >= 0 && temp < 32 && check == 1)
        {
            second = temp;
            check = 0;
            if (temp == 9)
            {
                int c = 0;
            }
            arr[first][second]++;
            n++;
        }
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < m; j++)
        {
            arr[i][j] /= n;
        }
    }

}
void mostBigrams(int(&most_bigrams)[MB][2], double(&amount)[M][M]) 
{        
    double maxs[MB];
    for (int h = 0; h < MB; h++)
    {
        double max = 0;
        int im = -1;
        int jm = -1;
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < M; j++)
            {
                if (h > 0)
                {
                    if (amount[i][j] > max && amount[i][j] < maxs[h - 1] && (j != most_bigrams[h - 1][1] || i != most_bigrams[h - 1][0]))
                    {
                        max = amount[i][j];
                        jm = j;
                        im = i;
                    }
                }
                else 
                {
                    if (amount[i][j] > max)
                    {
                        max = amount[i][j];
                        jm = j;
                        im = i;
                    }
                }
            }
        }        
        most_bigrams[h][0] = im;
        most_bigrams[h][1] = jm;
        maxs[h] = max;
        cout << endl << im << " " << jm << " " << max;
    }    
}
void solve(int X1, int X2, int Y1, int Y2, int& a, int& b)
{
    int temp = turnedEl(X1 - X2, M * M);
    a = (temp * (Y1 - Y2)) % (M * M);
    if (a < 0)
    {
        a += M * M;
    }
    b = (Y1 - a * X1) % (M * M);
    if (b < 0)
    {
        b += M * M;
    }
}
string shifr(string Text, int* alphabet, int a, int b)
{
    string shifred_text = "";
    for (int i = 0; i < size(Text); i += 2)
    {
        int first = (int)Text[i] + 32;
        int second = (int)Text[i + 1] + 32;
        if (first == 27 && A26 == 27)
        {
            first--;
        }
        if (first == 28 && A27 == 28)
        {
            first = 27;
        }
        if (first == 28 && A27 == 27)
        {
            first = 26;
        }
        if (second == 27 && A26 == 27)
        {
            second--;
        }
        if (second == 28 && A27 == 28)
        {
            second = 27;
        }
        if (second == 28 && A27 == 27)
        {
            second = 26;
        }
        if (first > 28)
        {
            first--;
        }
        if (second > 28)
        {
            second--;
        }
        int X = first * M + second;
        int Y = (a * X + b) % (M * M);
        shifred_text.push_back((char)(alphabet[Y / M] - 32));
        shifred_text.push_back((char)(alphabet[Y % M] - 32));
    }
    return shifred_text;
}
string deshifr(string Shifr, int* alphabet, int a, int b)
{
    string deshifred_text = "";
    for (int i = 0; i < size(Shifr); i += 2)
    {
        int first = (int)Shifr[i] + 32;
        int second = (int)Shifr[i + 1] + 32;
        if (first == 27 && A26 == 27)
        {
            first--;
        }
        if (first == 28 && A27 == 28)
        {
            first = 27;
        }
        if (first == 28 && A27 == 27)
        {
            first = 26;
        }
        if (second == 27 && A26 == 27)
        {
            second--;
        }
        if (second == 28 && A27 == 28)
        {
            second = 27;
        }
        if (second == 28 && A27 == 27)
        {
            second = 26;
        }
        if (first > 28)
        {
            first--;
        }
        if (second > 28)
        {
            second--;
        }
        int X = first * M + second;
        int Y = (turnedEl(a, M * M) * (X - b)) % (M * M);
        if (Y < 0)
        {
            Y += M * M;
        }
        deshifred_text.push_back((char)(alphabet[Y / M] - 32));
        deshifred_text.push_back((char)(alphabet[Y % M] - 32));
    }
    return deshifred_text;
}
int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    setlocale(LC_ALL, "Russian");
    string name = "Text.txt";
    string text1 = readFile(name);
    string text2 = readFile("Shifr.txt");
    double amount[M][M];
    double shifr_amount[M][M];
    int alphabet[31] = { 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,A26,A27,29,30,31 };
    for (int i = 0; i < M; i++)
    {
        cout << char(alphabet[i] - 32) << " " << i << endl;
    }
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < M; j++)
        {
            amount[i][j] = 0;
            shifr_amount[i][j] = 0;
        }
    }

    bigrams(text1, amount);
    bigrams(text2, shifr_amount);
    int maxB[MB][2];
    int shifrMaxB[MB][2];
    int** t1 = new int* [MB];
    for (int i = 0; i < MB; i++)
    {
        t1[i] = new int[2];
    }
    for (int i = 0; i < M; i++)
    {
        cout << endl;
        //for (int j = 0; j < M; j++)
        //{
        //    double x = round(amount[i][j] * 1000) / 1000;
        //    string temp = to_string(x);
        //    string prnt = "";
        //    for (int h = 0; h < 5; h++)
        //    {
        //        prnt.push_back(temp[h]);
        //    }
        //    prnt.push_back(' ');
        //    cout << prnt;
        //}
    }
    mostBigrams(maxB, amount);
    mostBigrams(shifrMaxB, shifr_amount);
    for (int i = 0; i < MB; i++)
    {
        for (int j = 0; j < MB; j++)
        {
            if (i != j)
            {
                int X1 = maxB[i][0] * M + maxB[i][1];
                int X2 = maxB[j][0] * M + maxB[j][1];
                int Y1 = shifrMaxB[i][0] * M + shifrMaxB[i][1];
                int Y2 = shifrMaxB[j][0] * M + shifrMaxB[j][1];
                int a = 0;
                int b = 0;
                solve(X1, X2, Y1, Y2, a, b);
                if (a != 0 && b != 0)
                {
                    cout << a << " " << b << endl;
                    if (a == 99)
                    {
                        string res = deshifr(text2, alphabet, a, b);
                        cout << res;
                    }
                    double temp_bigrams[M][M];
                    for (int i = 0; i < M; i++)
                    {
                        for (int j = 0; j < M; j++)
                        {
                            temp_bigrams[i][j] = 0;
                        }
                    }
                    string res = deshifr(text2, alphabet, a, b);
                    bigrams(res, temp_bigrams);
                    if (temp_bigrams[1][9] > 0 || temp_bigrams[2][9] > 0 || temp_bigrams[3][9] > 0 || temp_bigrams[4][9] > 0
                        || temp_bigrams[6][9] > 0 || temp_bigrams[7][10] > 0 || temp_bigrams[11][9] > 0
                        || temp_bigrams[12][9] > 0 || temp_bigrams[13][9] > 0 || temp_bigrams[15][9] > 0 || temp_bigrams[20][9] > 0
                        || temp_bigrams[16][9] > 0 || temp_bigrams[17][9] > 0 || temp_bigrams[18][9] > 0 || temp_bigrams[21][9] > 0
                        || temp_bigrams[22][9] > 0 || temp_bigrams[23][9] > 0 || temp_bigrams[24][9] > 0 || temp_bigrams[25][9] > 0
                        )
                    {
                        continue;
                    }
                    cout << endl << a << " " << b;
                    cout << endl << res;
                }
            }
        }
    }
    string test1 = shifr(text1, alphabet, 10, 10);
    string test2 = deshifr(test1, alphabet, 10, 10);
    //cout << endl << test2;
    return 0;
}