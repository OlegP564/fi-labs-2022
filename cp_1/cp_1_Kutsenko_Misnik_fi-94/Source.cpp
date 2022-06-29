#include <iostream>
#include <string>
#include <map>
#include <cctype>
#include <algorithm>
#include <Windows.h>
#include <fstream>
#include <fcntl.h>
#include <sys\types.h>
#include <sys\stat.h>
#include <io.h>
#include <vector>

using namespace std;

//string etalon = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";
string etalon = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя ";

int main()
{
    setlocale(0, "Rus");
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    string path = "bigram.txt";
    string str;

    ifstream fin;
    fin.open(path);

    if (!fin.is_open()) 
    {
        cout << "Ошибка открытия файла!" << endl;
    }
    else
    {
        while (!fin.eof())
        {
            str = "";
            getline(fin, str);
        }
    }
    fin.close();

    int length = 0;
    double  H1 = 0, H2 = 0, H3 = 0;

    //getline(cin, str);

    for (int i = 0; i < str.length(); i++) {
        if (etalon.find(tolower(str[i])) != string::npos) {
            length++;
        }
    }

    map<char, double> mp;
    for (auto e : str) {
        if (etalon.find(tolower(e)) != string::npos) {
            ++mp[tolower(e)];
        }
    }
    for (auto& pair : mp) {
        cout << "char: " << pair.first << " | count: " << pair.second / length << endl; 
        H1 = H1 - ((pair.second / length) * log2(pair.second / length));
    }
    cout << "H1 = " << H1 << endl;

    size_t position = str.find_first_of(";:.,/?-!*+=()&^%$@#1234567890—«»“”");

    while (position != string::npos)
    {
        str.erase(position, 1);
        position = str.find_first_of(";:.,/?-!*+=()&^%$@#1234567890—«»“”");
    }

    for (int i = 0; i <= str.length() - 1; ++i) {
        str[i] = tolower(str[i]);
    }

    for (int j = 0; j <= etalon.length() - 1; ++j)
    {
        for (int k = 0; k <= etalon.length() - 1; ++k)
        {
            double count = 0;
            for (int i = 0; i <= str.length() - 1; ++i)
            {
                if (str[i] == etalon[j] && str[i + 1] == etalon[k]) {
                    count++;
                }
            }
            if (count != 0) {
                cout << '[' << etalon[j] << ", " << etalon[k] << "]: " << count / (str.length() - 1) << endl;
                H2 = H2 - ((count / (str.length() - 1)) * log2(count / (str.length() - 1)));
            }
        }
    }
    cout << "H2 = " << H2 << endl;

    for (int j = 0; j <= etalon.length() - 1; ++j)
    {
        for (int k = 0; k <= etalon.length() - 1; ++k)
        {
            double count1 = 0;
            for (int i = 0; i <= str.length() - 1; i = i + 2)
            {
                if (str[i] == etalon[j] && str[i + 1] == etalon[k]) {
                    count1++;
                }
            }
            if (count1 != 0) {
                cout << '[' << etalon[j] << ", " << etalon[k] << "]: " << count1 / ((str.length() - 1) / 2) << endl;
                H3 = H3 - ((count1 / ((str.length() - 1) / 2)) * log2(count1 / ((str.length() - 1) / 2)));
            }
        }
    }
    cout << "H3 = " << H3 << endl;

    return 0;
}
