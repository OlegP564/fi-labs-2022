#include <iostream>
#include "windows.h"
#include <fstream>
#include <string>
using namespace std;

string VigSH(string Text, string Key)
{
	string Veg = Text;
	for (int i = 0; i < size(Text); i++)
	{
		int temp;
		temp = (static_cast<int>(Text[i]) + static_cast<int>(Key[i % size(Key)])) % 32;
		if (temp == 0)
			Veg[i] = -32;
		else
			Veg[i] = temp;
	}
	return Veg;
}
string DeVig(string Veg, string Key)
{
	string Text = Veg;
	for (int i = 0; i < size(Text); i++)
	{
		int temp = 0;
		temp = ((static_cast<int>(Veg[i]) - static_cast<int>(Key[i % size(Key)])) % 32);
		if (temp == 0)
			temp = temp - 32;
		else if (temp > 0)
			temp = temp - 32;
		Text[i] = temp;
	}
	return Text;
}
string Filter(string Junk)
{
	string Norm = Junk;
	for (int i = 0; i < size(Norm); i++)
	{
		int temp = static_cast<int>(Norm[i]);
		if ((temp < -32 && temp >= -64))
			Norm[i] = temp + 32;
		else if (temp > 0 || temp < -64)
		{
			Norm.erase(i, 1);
			i--;
		}

	}
	return Norm;
}
double IndexVidpov(string Text)
{
	double In = 0;
	double amount[32];
	for (int i = 0; i < 32; i++)
		amount[i] = 0;
	for (int i = 0; i < size(Text); i++)
		amount[static_cast<int>(Text[i]) + 32]++;
	for (int i = 0; i < 32; i++)
	{
		In = In + amount[i] * (amount[i] - 1) / (size(Text) * (size(Text) - 1));
	}
	return In;
}
int Dist(string Text)
{
	int max = 0;
	int amount = 0;
	for (int i = 5; i <= 30; i++)
	{
		int temp = 0;
		for (int j = 0; j < size(Text) - i; j++)
		{
			if (Text[j] == Text[j + i])
				temp++;
		}
		if (temp > amount)
		{
			max = i;
			amount = temp;
		}
		cout << "for " << i << " = " << temp << endl;
	}
	return max;
}
int main()
{
	ifstream fin("Text.txt");
	ifstream shin("Shifr.txt");
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	setlocale(LC_ALL, "Russian");
	//char ABC[34] = "јЅ¬√ƒ≈®∆«»… ЋћЌќѕ–—“”‘’÷„ЎўЏџ№Ёёя";
	string Key2, Key3, Key4, Key5, Key15, Key20, Key25, Key26, Key27, Key28, Key29,Key30;
	string Sh2, Sh3, Sh4, Sh5, Sh15 , Sh20, Sh25, Sh26, Sh27, Sh28, Sh29, Sh30;
	double In2, In3, In4, In5, In15, In20, In25, In26, In27, In28, In29, In30, InSh;
	string JunkText;
	string Text;
	string JunkShifr;
	string Shifr;
	getline(fin, JunkText);
	getline(shin, JunkShifr);
	Shifr = Filter(JunkShifr);
	Text = Filter(JunkText);
	Key2 = "н€";
	Key3 = "м€у";
	Key4 = "буба";
	Key5 = "парус";
	Key15 = "совершенствован";
	Key20 = "усовершенствованство";
	Key25 = "усовершенствованствопарус";
	Key26 = "фывапролджйцукенгшвапрсч€ы";
	Key27 = "фывапролджйцукенгшвапрсч€ыу";
	Key28 = "фывапролджйцукенгшвапрсч€ыук";
	Key29 = "фывапролджйцукенгшвапрсч€ыука";
	Key30 = "фывапролджйцукенгшвапрсч€ыукас";
	Sh2 = VigSH(Text, Key2);
	Sh3 = VigSH(Text, Key3);
	Sh4 = VigSH(Text, Key4);
	Sh5 = VigSH(Text, Key5);
	Sh15 = VigSH(Text, Key15);
	Sh20 = VigSH(Text, Key20);
	Sh25 = VigSH(Text, Key25);
	Sh26 = VigSH(Text, Key26);
	Sh27 = VigSH(Text, Key27);
	Sh28 = VigSH(Text, Key28);
	Sh29 = VigSH(Text, Key29);
	Sh30 = VigSH(Text, Key30);
	In2 = IndexVidpov(Sh2);
	In3 = IndexVidpov(Sh3);
	In4 = IndexVidpov(Sh4);
	In5 = IndexVidpov(Sh5);
	In15 = IndexVidpov(Sh15);
	In20 = IndexVidpov(Sh20);
	In25 = IndexVidpov(Sh25);
	In26 = IndexVidpov(Sh26);
	In27 = IndexVidpov(Sh27);
	In28 = IndexVidpov(Sh28);
	In29 = IndexVidpov(Sh29);
	In30 = IndexVidpov(Sh30);
	InSh = IndexVidpov(Shifr);
	cout << "Shifrotext for 2 : "<< endl << Sh2 << endl;
	cout << "Shifrotext for 3 : "<< endl << Sh3 << endl;
	cout << "Shifrotext for 4 : "<< endl << Sh4 << endl;
	cout << "Shifrotext for 5 : "<< endl << Sh5 << endl;
	cout << "Shifrotext for 15 : "<< endl << Sh15 << endl;
	cout << "Shifrotext for Shifr : " << endl << Shifr << endl;
	cout<<"Index vidpovidnosty for 2 = "<< In2 << endl;
	cout<<"Index vidpovidnosty for 3 = "<< In3 << endl;
	cout<<"Index vidpovidnosty for 4 = "<< In4 << endl;
	cout<<"Index vidpovidnosty for 5 = "<< In5 << endl;
	cout<<"Index vidpovidnosty for 15 = "<< In15 << endl;
	cout << "Index vidpovidnosty for 20 = " << In20 << endl;
	cout << "Index vidpovidnosty for 25 = " << In25 << endl;
	cout << "Index vidpovidnosty for 26 = " << In26 << endl;
	cout << "Index vidpovidnosty for 27 = " << In27 << endl;
	cout << "Index vidpovidnosty for 28 = " << In28 << endl;
	cout << "Index vidpovidnosty for 29 = " << In29 << endl;
	cout << "Index vidpovidnosty for 30 = " << In30 << endl;
	cout << "Index vidpovidnosty for Shifr = " << InSh << endl;
	cout << "r = " << Dist(Shifr) << endl;
	int r = Dist(Shifr);
	double Mi[17][32];
	for (int i = 0; i < 17; i++)
		for (int j = 0; j < 32; j++)
			Mi[i][j] = 0;
	double pt[32] = { 0.0794447,0.0143855,0.0443362 ,0.0206028 ,0.0274271 ,0.0873743 ,0.00717175 ,0.0156988 ,0.0866165 ,0.0146451 ,0.0344252 ,0.0419959 ,0.0323922 ,0.0680161 ,0.101601 ,0.0260756 ,0.0555243 ,0.0546767 ,0.0600598 ,0.0209827 ,0.00541174 ,0.0105219 ,0.00708203 ,0.0126427 ,0.00565035 ,0.0032795 ,0.0003,0.018314 ,0.013152,0.00382353,0.00627457, 0.020095 };
	//тут знаходитьс€ функц≥€ ћ≥(g) , вже в наступн≥й лаб≥ буду працювати з функц≥€ми , €к≥ повертають масиви
	for (int i = 0; i < r; i++)
	{
		for (int g = 0; g < 32; g++)
		{
			for (int t = 0; t < 32; t++)
			{
				int x = g + t;
				for (int b = 0; b < size(Shifr) / r; b++)
				{
					if ((static_cast<int>(Shifr[i + r * b]) + 32) == x)
						Mi[i][g] = Mi[i][g] + pt[t];
				}
			}
		}
	}
	for (int i = 0; i < 17; i++)
	{
		int max = 0;
		double temp = 0;
		for (int j = 0; j < 32; j++)
		{
			if (Mi[i][j] > temp)
			{
				temp = Mi[i][j];
				max = j;
			}

		}
		char ch(max - 32);
		cout << ch;
	}
	cout << endl;
	string KeyKey = "родинабезразлична";
	string KeyKey1 = "родинабезразвити€";
	string KeyKey2 = "родинабезразличи€";
	cout << DeVig(Shifr, KeyKey2);
	return 0;
}