#include <iostream>;
#include <string>;
#include "windows.h";
#include <fstream>;
#include <iomanip> 
using namespace std;
int main()
{
	
	ifstream fin("Text.txt");
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	setlocale(LC_ALL, "Russian");
	string StartText;
	getline(fin, StartText);
	int amount[32];
	for (int i = 0; i < 32; i++)
		amount[i] = 0;
	int amount2[33][33];
	for (int i = 0; i < 33; i++)
		for (int j = 0; j < 33; j++)
			amount2[i][j] = 0;
	int amount2_peresechless[33][33];
	for (int i = 0; i < 33; i++)
		for (int j = 0; j < 33; j++)
			amount2_peresechless[i][j] = 0;
	int counter = 0;
	for (int i = 0; i < size(StartText); i++)
	{
		if (StartText[i] == 'À'|| StartText[i] == 'à')
		{
			StartText[i] = 'à';
			amount[0]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][0]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][0]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][0]++;
				else
					amount2[32][0]++;
			continue;
		}
		if (StartText[i] == 'Á' || StartText[i] == 'á')
		{
			StartText[i] = 'á';
			amount[1]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][1]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][1]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][1]++;
				else
					amount2[32][1]++;
			continue;
		}
		if (StartText[i] == 'Â' || StartText[i] == 'â')
		{
			StartText[i] = 'â';
			amount[2]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][2]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][2]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][2]++;
				else
					amount2[32][2]++;
		    continue;
		}
		if (StartText[i] == 'Ã'|| StartText[i] == 'ã')
		{
			StartText[i] = 'ã';
			amount[3]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][3]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][3]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][3]++;
				else
					amount2[32][3]++;
			continue;
		}
		if (StartText[i] == 'Ä'|| StartText[i] == 'ä')
		{
			StartText[i] = 'ä';
			amount[4]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][4]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][4]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][4]++;
				else
					amount2[32][4]++;
			continue;
		}
		if (StartText[i] == 'Å'|| StartText[i] == 'å'||StartText[i] == '¸' || StartText[i] == '¨')
		{
			StartText[i] = 'å';
			amount[5]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][5]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][5]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][5]++;
				else
					amount2[32][5]++;
			continue;
		}
		if (StartText[i] == 'Æ'|| StartText[i] == 'æ')
		{
			StartText[i] = 'æ';
			amount[6]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][6]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][6]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][6]++;
				else
					amount2[32][6]++;
			continue;
		}
		if (StartText[i] == 'Ç'|| StartText[i] == 'ç')
		{
			StartText[i] = 'ç';
			amount[7]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][7]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][7]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][7]++;
				else
					amount2[32][7]++;
			continue;
		}
		if (StartText[i] == 'È'|| StartText[i] == 'è')
		{
			StartText[i] = 'è';
			amount[8]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][8]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][8]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][8]++;
				else
					amount2[32][8]++;
			continue;
		}
		if (StartText[i] == 'É'|| StartText[i] == 'é')
		{
			StartText[i] = 'é';
			amount[9]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][9]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][9]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][9]++;
				else
					amount2[32][9]++;
			continue;
		}
		if (StartText[i] == 'Ê'|| StartText[i] == 'ê')
		{
			StartText[i] = 'ê';
			amount[10]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][10]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][10]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][10]++;
				else
					amount2[32][10]++;
			continue;
		}
		if (StartText[i] == 'Ë'|| StartText[i] == 'ë')
		{
			StartText[i] = 'ë';
			amount[11]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][11]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][11]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][11]++;
				else
					amount2[32][11]++;
			continue;
		}
		if (StartText[i] == 'Ì'|| StartText[i] == 'ì')
		{
			StartText[i] = 'ì';
			amount[12]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][12]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][12]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][12]++;
				else
					amount2[32][12]++;
			continue;
		}
		if (StartText[i] == 'Í'|| StartText[i] == 'í')
		{
			StartText[i] = 'í';
			amount[13]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][13]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][13]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][13]++;
				else
					amount2[32][13]++;
			continue;
		}
		if (StartText[i] == 'Î'|| StartText[i] == 'î')
		{
			StartText[i] = 'î';
			amount[14]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][14]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][14]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][14]++;
				else
					amount2[32][14]++;
			continue;
		}
		if (StartText[i] == 'Ï'|| StartText[i] == 'ï')
		{
			StartText[i] = 'ï';
			amount[15]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][15]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][15]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][15]++;
				else
					amount2[32][15]++;
			continue;
		}
		if (StartText[i] == 'Ð'|| StartText[i] == 'ð')
		{
			StartText[i] = 'ð';
			amount[16]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][16]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][16]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][16]++;
				else
					amount2[32][16]++;
			continue;
		}
		if (StartText[i] == 'Ñ'|| StartText[i] == 'ñ')
		{
			StartText[i] = 'ñ';
			amount[17]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][17]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][17]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][17]++;
				else
					amount2[32][17]++;
			continue;
		}
		if (StartText[i] == 'Ò'|| StartText[i] == 'ò')
		{
			StartText[i] = 'ò';
			amount[18]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][18]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][18]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][18]++;
				else
					amount2[32][18]++;
			continue;
		}
		if (StartText[i] == 'Ó'|| StartText[i] == 'ó')
		{
			StartText[i] = 'ó';
			amount[19]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][19]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][19]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][19]++;
				else
					amount2[32][19]++;
			continue;
		}
		if (StartText[i] == 'Ô'|| StartText[i] == 'ô')
		{
			StartText[i] = 'ô';
			amount[20]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][20]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][20]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][20]++;
				else
					amount2[32][20]++;
			continue;
		}
		if (StartText[i] == 'Õ'|| StartText[i] == 'õ')
		{
			StartText[i] = 'õ';
			amount[21]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][21]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][21]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][21]++;
				else
					amount2[32][21]++;
			continue;
		}
		if (StartText[i] == 'Ö'|| StartText[i] == 'ö')
		{
			StartText[i] = 'ö';
			amount[22]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][22]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][22]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][22]++;
				else
					amount2[32][22]++;
			continue;
		}
		if (StartText[i] == '×'|| StartText[i] == '÷')
		{
			StartText[i] = '÷';
			amount[23]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][23]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][23]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][23]++;
				else
					amount2[32][23]++;
			continue;
		}
		if (StartText[i] == 'Ø'|| StartText[i] == 'ø')
		{
			StartText[i] = 'ø';
			amount[24]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][24]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][24]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][24]++;
				else
					amount2[32][24]++;
			continue;
		}
		if (StartText[i] == 'Ù'|| StartText[i] == 'ù')
		{
			StartText[i] = 'ù';
			amount[25]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][25]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][25]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][25]++;
				else
					amount2[32][25]++;
			continue;
		}
		if (StartText[i] == 'Û'|| StartText[i] == 'û')
		{
			StartText[i] = 'û';
			amount[26]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][27]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][27]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][27]++;
				else
					amount2[32][27]++;
			continue;
		}
		if (StartText[i] == 'Ú'||StartText[i] == 'ú'|| StartText[i] == 'ü'|| StartText[i] == 'Ü')
		{
			StartText[i] = 'ü';
			amount[27]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][28]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][28]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][28]++;
				else
					amount2[32][28]++;
			continue;
		}
		if (StartText[i] == 'Ý'|| StartText[i] == 'ý')
		{
			StartText[i] = 'ý';
			amount[28]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][29]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][29]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][29]++;
				else
					amount2[32][29]++;
			continue;
		}
		if (StartText[i] == 'Þ'|| StartText[i] == 'þ')
		{
			StartText[i] = 'þ';
			amount[29]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][30]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][30]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][30]++;
				else
					amount2[32][30]++;
			continue;
		}
		if (StartText[i] == 'ß'||StartText[i] == 'ÿ')
		{
			StartText[i] = 'ÿ';
			amount[30]++;
			counter++;
			if (i != 0 && StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][31]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][31]++;
			if (i != 0)
				if (StartText[i - 1] != ' ')
					amount2[static_cast<int>(StartText[i - 1]) + 32][31]++;
				else
					amount2[32][31]++;
			continue;
		}
		if (StartText[i] == ' ' && i != size(StartText) - 1 && i != 0 && StartText[i - 1] != ' ')
		{
			amount[31]++;
			counter++;
			if (StartText[i - 1] != ' ' && counter % 2 == 0)
				amount2_peresechless[static_cast<int>(StartText[i - 1]) + 32][32]++;
			else if (counter % 2 == 0)
				amount2_peresechless[32][32]++;
			if (i != 0)
				amount2[static_cast<int>(StartText[i - 1]) + 32][32]++;
			continue;
		}
		StartText.erase(i, 1);
		i--;
	}
	//char abc[35] = " àáâãäå¸æçèéêëìíîïðñòóôõö÷øùúûüýþÿ";
	double H1 = 0;
	double H2 = 0;
	double H2_peresechless = 0;
	cout << size(StartText) << endl;
	for (int i = 0; i < 32; i++)
	{
		double p =(double)amount[i] / (double)(size(StartText));
		H1 = H1 + p * (log(size(StartText)) / log(2) - log(amount[i]) / log(2));
	}
	for(int i = 0; i < 33; i ++)
		for (int j = 0; j < 33; j++)
		{
			if (amount2[i][j] != 0)
			{
				double p = (double)amount2[i][j] / (double)((size(StartText)-1));
				H2 = H2 + p * (log(size(StartText) - 1) / log(2) - log(amount2[i][j]) / log(2));
			}
		}
	for (int i = 0; i < 33; i++)
		for (int j = 0; j < 33; j++)
		{
			if (amount2_peresechless[i][j] != 0)
			{
				double p = (double)amount2_peresechless[i][j] / (double)(size(StartText)/2);
				H2_peresechless = H2_peresechless + p * (log(size(StartText)/2) / log(2) - log(amount2_peresechless[i][j]) / log(2));
			}
		}
	cout << "H1: " << H1 << endl;
	cout << "H2: " << H2 << endl;
	cout << "H2_peretynless: " << H2_peresechless << endl;
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	string SpacelessText = StartText;
	int spaceless_counter = 0;
	int amount_spaceless[31];
	for (int i = 0; i < 31; i++)
		amount_spaceless[i] = 0;
	int amount2_spaceless[32][32];
	int amount2_spaceless_peresechless[32][32];
	for (int i = 0; i < 32; i++)
		for (int j = 0; j < 32; j++)
			amount2_spaceless[i][j] = 0;
	for (int i = 0; i < 32; i++)
		for (int j = 0; j < 32; j++)
			amount2_spaceless_peresechless[i][j] = 0;
	for (int i = 0; i < size(SpacelessText); i++)
	{
		if (SpacelessText[i] == 'À' || SpacelessText[i] == 'à')
		{
			SpacelessText[i] = 'à';
			amount_spaceless[0]++;
			spaceless_counter++;
			if(spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][0]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][0]++;
			continue;
		}
		if (SpacelessText[i] == 'Á' || SpacelessText[i] == 'á')
		{
			SpacelessText[i] = 'á';
			amount_spaceless[1]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][1]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][1]++;
			continue;
		}
		if (SpacelessText[i] == 'Â' || SpacelessText[i] == 'â')
		{
			SpacelessText[i] = 'â';
			amount_spaceless[2]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][2]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][2]++;
			continue;
		}
		if (SpacelessText[i] == 'Ã' || SpacelessText[i] == 'ã')
		{
			SpacelessText[i] = 'ã';
			amount_spaceless[3]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][3]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][3]++;
			continue;
		}
		if (SpacelessText[i] == 'Ä' || SpacelessText[i] == 'ä')
		{
			SpacelessText[i] = 'ä';
			amount_spaceless[4]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][4]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][4]++;
			continue;
		}
		if (SpacelessText[i] == 'Å' || SpacelessText[i] == 'å' || SpacelessText[i] == '¸' || SpacelessText[i] == '¨')
		{
			SpacelessText[i] = 'å';
			amount_spaceless[5]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][5]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][5]++;
			continue;
		}
		if (SpacelessText[i] == 'Æ' || SpacelessText[i] == 'æ')
		{
			SpacelessText[i] = 'æ';
			amount_spaceless[6]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][6]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][6]++;
			continue;
		}
		if (SpacelessText[i] == 'Ç' || SpacelessText[i] == 'ç')
		{
			SpacelessText[i] = 'ç';
			amount_spaceless[7]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][7]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][7]++;
			continue;
		}
		if (SpacelessText[i] == 'È' || SpacelessText[i] == 'è')
		{
			SpacelessText[i] = 'è';
			amount_spaceless[8]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][8]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][8]++;
			continue;
		}
		if (SpacelessText[i] == 'É' || SpacelessText[i] == 'é')
		{
			SpacelessText[i] = 'é';
			amount_spaceless[9]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][9]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(StartText[i - 1]) + 32][9]++;
			continue;
		}
		if (SpacelessText[i] == 'Ê' || SpacelessText[i] == 'ê')
		{
			SpacelessText[i] = 'ê';
			amount_spaceless[10]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][10]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][10]++;
			continue;
		}
		if (SpacelessText[i] == 'Ë' || SpacelessText[i] == 'ë')
		{
			SpacelessText[i] = 'ë';
			amount_spaceless[11]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][11]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][11]++;
			continue;
		}
		if (SpacelessText[i] == 'Ì' || SpacelessText[i] == 'ì')
		{
			SpacelessText[i] = 'ì';
			amount_spaceless[12]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][12]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][12]++;
			continue;
		}
		if (SpacelessText[i] == 'Í' || SpacelessText[i] == 'í')
		{
			SpacelessText[i] = 'í';
			amount_spaceless[13]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][13]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][13]++;
			continue;
		}
		if (SpacelessText[i] == 'Î' || SpacelessText[i] == 'î')
		{
			SpacelessText[i] = 'î';
			amount_spaceless[14]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][14]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][14]++;
			continue;
		}
		if (SpacelessText[i] == 'Ï' || SpacelessText[i] == 'ï')
		{
			SpacelessText[i] = 'ï';
			amount_spaceless[15]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][15]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][15]++;
			continue;
		}
		if (SpacelessText[i] == 'Ð' || SpacelessText[i] == 'ð')
		{
			SpacelessText[i] = 'ð';
			amount_spaceless[16]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][16]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][16]++;
			continue;
		}
		if (SpacelessText[i] == 'Ñ' || SpacelessText[i] == 'ñ')
		{
			SpacelessText[i] = 'ñ';
			amount_spaceless[17]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][17]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][17]++;
			continue;
		}
		if (SpacelessText[i] == 'Ò' || SpacelessText[i] == 'ò')
		{
			SpacelessText[i] = 'ò';
			amount_spaceless[18]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][18]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][18]++;
			continue;
		}
		if (SpacelessText[i] == 'Ó' || SpacelessText[i] == 'ó')
		{
			SpacelessText[i] = 'ó';
			amount_spaceless[19]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][19]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][19]++;
			continue;
		}
		if (SpacelessText[i] == 'Ô' || SpacelessText[i] == 'ô')
		{
			SpacelessText[i] = 'ô';
			amount_spaceless[20]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][20]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][20]++;
			continue;
		}
		if (SpacelessText[i] == 'Õ' || SpacelessText[i] == 'õ')
		{
			SpacelessText[i] = 'õ';
			amount_spaceless[21]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][21]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][21]++;
			continue;
		}
		if (SpacelessText[i] == 'Ö' || SpacelessText[i] == 'ö')
		{
			SpacelessText[i] = 'ö';
			amount_spaceless[22]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][22]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][22]++;
			continue;
		}
		if (SpacelessText[i] == '×' || SpacelessText[i] == '÷')
		{
			SpacelessText[i] = '÷';
			amount_spaceless[23]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][23]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][23]++;
			continue;
		}
		if (SpacelessText[i] == 'Ø' || SpacelessText[i] == 'ø')
		{
			SpacelessText[i] = 'ø';
			amount_spaceless[24]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][24]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][24]++;
			continue;
		}
		if (SpacelessText[i] == 'Ù' || SpacelessText[i] == 'ù')
		{
			SpacelessText[i] = 'ù';
			amount_spaceless[25]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][25]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][25]++;
			continue;
		}
		if (SpacelessText[i] == 'Û' || SpacelessText[i] == 'û')
		{
			SpacelessText[i] = 'û';
			amount_spaceless[26]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][27]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][27]++;
			continue;
		}
		if (SpacelessText[i] == 'Ú' || SpacelessText[i] == 'ú' || SpacelessText[i] == 'ü' || SpacelessText[i] == 'Ü')
		{
			SpacelessText[i] = 'ü';
			amount_spaceless[27]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][28]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][28]++;
			continue;
		}
		if (SpacelessText[i] == 'Ý' || SpacelessText[i] == 'ý')
		{
			SpacelessText[i] = 'ý';
			amount_spaceless[28]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][29]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][29]++;
			continue;
		}
		if (SpacelessText[i] == 'Þ' || SpacelessText[i] == 'þ')
		{
			SpacelessText[i] = 'þ';
			amount_spaceless[29]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][30]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][30]++;
			continue;
		}
		if (SpacelessText[i] == 'ß' || SpacelessText[i] == 'ÿ')
		{
			SpacelessText[i] = 'ÿ';
			amount_spaceless[30]++;
			spaceless_counter++;
			if (spaceless_counter % 2 == 0 && i != 0)
				amount2_spaceless_peresechless[static_cast<int>(SpacelessText[i - 1]) + 32][31]++;
			if (i != 0)
				if (SpacelessText[i - 1] != ' ')
					amount2_spaceless[static_cast<int>(SpacelessText[i - 1]) + 32][31]++;
			continue;
		}
		//if (StartText[i] == ' ' && i != size(StartText) - 1 && i != 0 && StartText[i - 1] != ' ')
		//{
		//	amount[31]++;
		//	if (i != 0)
		//		amount2[static_cast<int>(StartText[i - 1]) + 32][32]++;
		//	continue;
		//}
		SpacelessText.erase(i, 1);
		i--;
	}
	double H1_spaceless = 0;
	double H2_spaceless = 0;
	double H2_spaceless_peresechless = 0;
	for (int i = 0; i < 31; i++)
	{
		double p = (double)amount_spaceless[i] / (double)(size(SpacelessText));
		H1_spaceless = H1_spaceless + p * (log(size(SpacelessText)) / log(2) - log(amount_spaceless[i]) / log(2));
		//cout << H1 << endl;
	}
	for (int i = 0; i < 32; i++)
		for (int j = 0; j < 32; j++)
		{
			if (amount2_spaceless[i][j] != 0)
			{
				double p = (double)amount2_spaceless[i][j] / (double)(size(SpacelessText)-1);
				H2_spaceless = H2_spaceless + p * (log(size(SpacelessText)-1) / log(2) - log(amount2_spaceless[i][j]) / log(2));
			}
		}
	for (int i = 0; i < 32; i++)
		for (int j = 0; j < 32; j++)
		{
			if (amount2_spaceless_peresechless[i][j] != 0)
			{
				double p = (double)amount2_spaceless_peresechless[i][j] / (double)(size(SpacelessText)/2);
				H2_spaceless_peresechless = H2_spaceless_peresechless + p * (log(size(SpacelessText)/2) / log(2) - log(amount2_spaceless_peresechless[i][j]) / log(2));
			}
		}
	cout << "H1 spaceless = " << H1_spaceless << endl;
	cout << "H2 spaceless = " << H2_spaceless << endl;
	cout << "H2 spaceless and peretynless = " << H2_spaceless_peresechless << endl;
	cout << "With space: " << endl;
	for (int i = 0; i < 31; i++)
	{
		if (i < 26)
		{
			char temp(i - 32);
			cout << temp << ": " << (double)amount[i] / (double)size(StartText) << endl;
		}
		else
		{
			char temp(i - 31);
			cout << temp << ": " << (double)amount[i] / (double)size(StartText) << endl;
		}
	}
	cout << " : " << (double)amount[31] / (double)size(StartText) << endl;
	cout << "Without space: " << endl;
	for (int i = 0; i < 31; i++)
	{
		if (i < 26)
		{
			char temp(i - 32);
			cout << temp << ": " << (double)amount_spaceless[i] / (double)size(SpacelessText) << endl;
		}
		else
		{
			char temp(i - 31);
			cout << temp << ": " << (double)amount_spaceless[i] / (double)size(SpacelessText) << endl;
		}
	}
	cout << endl;
	cout << endl;
	for (int i = 0; i < 15; i++)
	{
		char temp(i-32);
		if (i == 0)
			cout << "  ";
		cout << setw(12) << temp << "|";
	}
	cout << endl;
	for (int i = 0; i < 33; i++)
	{
		if (i == 32)
			cout << "_";
		char temp(i - 32);
		cout << temp << "|";
		for (int j = 0; j < 15; j++)
		{
			cout << setw(12) << (double)amount2[i][j] / (double)(size(StartText)-1) << "|";
		}
		cout << endl;
	}
	cout << endl;
	cout << endl;
	for (int i = 15; i < 32; i++)
	{
		char temp(i - 32);
		if (i == 15)
			cout << "  ";
		cout << setw(12) << temp << "|";
	}
	cout << setw(12) << "_" << "|" << endl;
	for (int i = 0; i < 33; i++)
	{
		if (i == 32)
			cout << " ";
		char temp(i - 32);
		cout << temp << "|";
		for (int j = 15; j < 33; j++)
		{
			cout << setw(12) << (double)amount2[i][j] / (double)(size(StartText)-1) << "|";
		}
		cout << endl;
	}

	///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	cout << endl;
	cout << endl;
	for (int i = 0; i < 15; i++)
	{
		char temp(i - 32);
		if (i == 0)
			cout << "  ";
		cout << setw(12) << temp << "|";
	}
	cout << endl;
	for (int i = 0; i < 33; i++)
	{
		if (i == 32)
			cout << "_";
		char temp(i - 32);
		cout << temp << "|";
		for (int j = 0; j < 15; j++)
		{
			cout << setw(12) << (double)amount2_peresechless[i][j] / (double)(size(StartText)/2) << "|";
		}
		cout << endl;
	}
	cout << endl;
	cout << endl;
	for (int i = 15; i < 32; i++)
	{
		char temp(i - 32);
		if (i == 15)
			cout << "  ";
		cout << setw(12) << temp << "|";
	}
	cout << setw(12) << "_" << "|" << endl;
	for (int i = 0; i < 33; i++)
	{
		if (i == 32)
			cout << " ";
		char temp(i - 32);
		cout << temp << "|";
		for (int j = 15; j < 33; j++)
		{
			cout << setw(12) << (double)amount2_peresechless[i][j] / (double)(size(StartText)/2) << "|";
		}
		cout << endl;
	}
	///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	cout << endl;
	cout << endl;
	for (int i = 0; i < 15; i++)
	{
		char temp(i - 32);
		if (i == 0)
			cout << "  ";
		cout << setw(12) << temp << "|";
	}
	cout << endl;
	for (int i = 0; i < 32; i++)
	{
		char temp(i - 32);
		cout << temp << "|";
		for (int j = 0; j < 15; j++)
		{
			cout << setw(12) << (double)amount2_spaceless[i][j] / (double)(size(SpacelessText)-1) << "|";
		}
		cout << endl;
	}
	cout << endl;
	cout << endl;
	for (int i = 15; i < 32; i++)
	{
		char temp(i - 32);
		if (i == 15)
			cout << "  ";
		cout << setw(12) << temp << "|";
	}
	cout << endl;
	for (int i = 0; i < 32; i++)
	{
		char temp(i - 32);
		cout << temp << "|";
		for (int j = 15; j < 32; j++)
		{
			cout << setw(12) << (double)amount2_spaceless[i][j] / (double)(size(SpacelessText)-1) << "|";
		}
		cout << endl;
	}
	//////////////////////////////////////////////////////////////////////
	cout << endl;
	cout << endl;
	for (int i = 0; i < 15; i++)
	{
		char temp(i - 32);
		if (i == 0)
			cout << "  ";
		cout << setw(12) << temp << "|";
	}
	cout << endl;
	for (int i = 0; i < 32; i++)
	{
		char temp(i - 32);
		cout << temp << "|";
		for (int j = 0; j < 15; j++)
		{
			cout << setw(12) << (double)amount2_spaceless_peresechless[i][j] / (double)(size(SpacelessText)/2) << "|";
		}
		cout << endl;
	}
	cout << endl;
	cout << endl;
	for (int i = 15; i < 32; i++)
	{
		char temp(i - 32);
		if (i == 15)
			cout << "  ";
		cout << setw(12) << temp << "|";
	}
	cout << endl;
	for (int i = 0; i < 32; i++)
	{
		char temp(i - 32);
		cout << temp << "|";
		for (int j = 15; j < 32; j++)
		{
			cout << setw(12) << (double)amount2_spaceless_peresechless[i][j] / (double)(size(SpacelessText)/2) << "|";
		}
		cout << endl;
	}
	cout << endl;
	cout << endl;
	for (int i = 0; i < 32; i++)
	{
		int num = 0;
		int temp = 0;
		for (int j = 0; j < 32; j++)
		{
			if (amount[num] < amount[j])
				num = j;
		}
		char tempchar;
		if (num < 26)
			tempchar = num - 32;
		else
			tempchar = num - 31;
		if (num == 31)
			tempchar = '_';
		cout << tempchar << ": " << (double)amount[num] / (double)size(StartText) << endl;
		amount[num] = 0;
	}
	cout << endl;
	cout << endl;
	for (int i = 0; i < 31; i++)
	{
		int num = 0;
		int temp = 0;
		for (int j = 0; j < 31; j++)
		{
			if (amount_spaceless[num] < amount_spaceless[j])
				num = j;
		}
		char tempchar;
		if (num < 26)
			tempchar = num - 32;
		else
			tempchar = num - 31;
		cout << tempchar << ": " << (double)amount_spaceless[num] / (double)size(SpacelessText) << endl;
		amount_spaceless[num] = 0;
	}
	return 0;
}