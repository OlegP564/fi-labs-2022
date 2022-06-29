import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {
    public static String readFile(String fname,ArrayList<Integer> arr){
        String res ="";
        try(FileReader reader = new FileReader(fname))
        {
            int c;
            while((c=reader.read())!=-1){
                if(arr.contains(c)){
                    res+=(char)c;
                }
            }
        }
        catch(IOException ex){

            System.out.println(ex.getMessage());
        }
        return res;
    }
    public static int gcd(int a, int b){
        if(a<0){
            a*=-1;
        }
        if(b<0){
            b*=-1;
        }
        if(b==0){
            return a;
        }
        return gcd(b, a%b);
    }
    public static int Evklid (int a, int n) {
        if(a<0){
            a*=-1;
        }
        int s1 = 1, s2 = 0;
        int t1 = 0, t2 = 1;
        int m =n;
        while(n != 0) {
            int quotient = a / n;
            int r = a % n;
            a = n;
            n = r;
            int tempS = s1 - s2 * quotient;
            s1 = s2;
            s2 = tempS;
            int tempR = t1 - t2 * quotient;
            t1 = t2;
            t2 = tempR;
        }
        if(s1 <0){
            s1=s1+m;
        }
        return s1;
    }
    public static void readBigrams(String text,ArrayList<Integer> arr,double [][]b02,int m1){

        int calcb02 = 0;
        int c;
        int indexPrev2 =-1;
        int indStep = 0;
        for(int i =0;i<text.length();i++){
            c = text.charAt(i);
            if(indStep>1){
                indStep=0;
            }
            int tempc = Character.toLowerCase(c)-1072;
            int tempIndex = -1;
            if(tempc>=0&&tempc<32){
                tempIndex=c;
            }
            if(tempIndex>=0){
                if(indStep==1){
                    if(arr.contains(c)&&arr.contains(indexPrev2)){
                        b02[arr.indexOf(indexPrev2)][arr.indexOf(c)]++;
                        calcb02++;
                    }
                }
            }
            if(indStep == 0&& tempIndex>=0){
                indexPrev2 = c;
            }
            if(tempIndex>=0){
                indStep++;
            }
        }
        for(int i=0;i<m1;i++){
            for(int j =0;j<m1;j++){
                b02[i][j]=b02[i][j]/calcb02;
            }
        }



    }
    public static String encrText(String text, int a,int b,int m,ArrayList<Integer> arr){
        String res ="";
        for(int i =0;i<(int)text.length()/2;i++){
            char x1 = text.charAt(i*2);
            char x2 = text.charAt(i*2+1);
            int X = arr.indexOf((int)x1)*m+arr.indexOf((int)x2);
            int Y = (a*X+b)%(m*m);
            char y1 = (char)(int)arr.get((int)(Y/m));
            char y2 = (char)(int)arr.get(Y%m);
            res+=y1;
            res+=y2;
        }

        return res;
    }
    public static String decrText(String text, int a,int b,int m,ArrayList<Integer> arr){
        String res ="";
        for(int i =0;i<(int)text.length()/2;i++){
            char y1 = text.charAt(i*2);
            char y2 = text.charAt(i*2+1);
            int Y = arr.indexOf((int)y1)*m+arr.indexOf((int)y2);
            int X = (Evklid(a,m*m)*(Y-b))%(m*m);
            if( X < 0){
                X +=m*m;
            }
            char x1 = (char)(int)arr.get((int)(X/m));
            char x2 = (char)(int)arr.get(X%m);
            res+=x1;
            res+=x2;
        }

        return res;
    }
    public static int[][] maxBigrams(double [][]bigrams,int m){
        int [][]maxInd = new int[10][2];
        double max =0;
        int imax = -1;
        int jmax = -1;
        for(int i0 =0;i0<10;i0++){
            double maxtemp = max;
            double itemp = imax;
            double jtemp = jmax;
            max = 0;
            imax =-1;
            jmax = -1;
            for(int i =0;i<m;i++){
                for(int j =0;j<m;j++){
                    if(i0==0){
                        if(max<bigrams[i][j]){
                            max = bigrams[i][j];
                            imax = i;
                            jmax = j;
                        }
                    }else{
                        if(max<bigrams[i][j]&&(bigrams[i][j]<=maxtemp&&(i!=itemp||j!=jtemp))){
                            max = bigrams[i][j];
                            imax = i;
                            jmax = j;
                        }
                    }
                }
            }
            maxInd[i0][0]=imax;
            maxInd[i0][1]=jmax;
        }
        return maxInd;
    }
    public static int[][] getAB(int X1,int X2,int Y1,int Y2,int m){


        int temp = Evklid(X1-X2,m*m);
        int a = (temp*(Y1-Y2))%(m*m);
        if(a<0){
            a+=m*m;
        }
        int b = (Y1-a*X1)%(m*m);
        if(b<0){
            b+=m*m;
        }
        if(a==0){
            int [][]res = {};
            return res;
        }
        int [][]res = {{a,b}};
        return res;



    }

    public static void main(String[]args){
        int [][]alphabet = {{0,1072}
                ,{1,1073}
                ,{2,1074}
                ,{3,1075}
                ,{4,1076}
                ,{5,1077}
                ,{6,1078}
                ,{7,1079}
                ,{8,1080}
                ,{9,1081}
                ,{10,1082}
                ,{11,1083}
                ,{12,1084}
                ,{13,1085}
                ,{14,1086}
                ,{15,1087}
                ,{16,1088}
                ,{17,1089}
                ,{18,1090}
                ,{19,1091}
                ,{20,1092}
                ,{21,1093}
                ,{22,1094}
                ,{23,1095}
                ,{24,1096}
                ,{25,1097}
                ,{26,1100}//,{26,1099}
                ,{27,1099}//,{27,1100}
                ,{28,1101}
                ,{29,1102}
                ,{30,1103}

        };
        //System.out.println(gcd(-16,8));
        String fname = "03.txt";
        String fname1 = "text0.txt";

        int m = 31;
        double [][]bigrams= new double[m][m];
        double [][]bigrams03 = new double[m][m];
        for(int i =0;i<m;i++){
            for(int j =0;j<m;j++){
                bigrams[i][j]=0;
                bigrams03[i][j]=0;
            }
        }
        ArrayList<Integer> alp = new ArrayList<>();
        for(int i =0;i<alphabet.length;i++){
            alp.add(alphabet[i][1]);
        }
        String textmain = readFile(fname1,alp);
        String text03 = readFile(fname,alp);
        readBigrams(textmain,alp,bigrams,m);
        readBigrams(text03,alp,bigrams03,m);
        double sum =0;

        /*for(int i =0;i<m;i++){
            for(int j =0;j<m;j++){
                sum+=bigrams[i][j];
                String s = String.format("%.4f",bigrams[i][j]);
                System.out.print(s + " " );
            }
            System.out.println();
        }*/
        int [][] maxInd03 = maxBigrams(bigrams03,m);
        int [][] maxIndMain = maxBigrams(bigrams,m);
        System.out.println("max bigrams for language");
        for(int i=0;i<10;i++){
            String s = String.format("%.4f",bigrams[maxIndMain[i][0]][maxIndMain[i][1]]);
            System.out.println(s + " "+maxIndMain[i][0]+" "+maxIndMain[i][1]);
        }
        System.out.println("max bigrams for crypt text");
        for(int i=0;i<10;i++){
            String s = String.format("%.4f",bigrams03[maxInd03[i][0]][maxInd03[i][1]]);
            System.out.println(s + " "+maxInd03[i][0]+" "+maxInd03[i][1]);
        }

        for(int i =0;i<10;i++){
            for(int j =0;j<10;j++){
                if(i!=j) {
                    int X1 = maxIndMain[i][0] * m + maxIndMain[i][1];
                    int X2 = maxIndMain[j][0] * m + maxIndMain[j][1];
                    int Y1 = maxInd03[i][0] * m + maxInd03[i][1];
                    int Y2 = maxInd03[j][0] * m + maxInd03[j][1];
                    int[][] res = getAB(X1, X2, Y1, Y2, m);
                    for (int i0 = 0; i0 < res.length; i0++) {
                        String rest = decrText(text03, res[i0][0], res[i0][1], m, alp);
                        for(int h =0;h<m;h++){
                            for(int j0 =0;j0<m;j0++){
                                bigrams[h][j0]=0;
                            }
                        }
                        readBigrams(rest,alp,bigrams,m);
                        if(bigrams[0][26]!=0){

                            continue;

                        }
                        if(bigrams[29][26]!=0){
                            continue;
                        }
                        if(bigrams[30][26]!=0){
                            continue;
                        }
                        if(bigrams[14][26]!=0){
                            continue;
                        }
                        if(bigrams[8][26]!=0){
                            continue;
                        }
                        if(bigrams[5][26]!=0){
                            continue;
                        }
                        if(bigrams[1][9]!=0){
                            continue;
                        }
                        if(bigrams[2][9]!=0){
                            continue;
                        }
                        if(bigrams[3][9]!=0){
                            continue;
                        }
                        if(bigrams[7][9]!=0){
                            continue;
                        }
                        if(bigrams[6][9]!=0){
                            continue;
                        }
                        if(bigrams[10][9]!=0){
                            continue;
                        }
                        if(bigrams[11][9]!=0){
                            continue;
                        }
                        if(bigrams[13][9]!=0){
                            continue;
                        }
                        if(bigrams[12][9]!=0){
                            continue;
                        }
                        if(bigrams[18][9]!=0){
                            continue;
                        }
                        if(bigrams[17][9]!=0){
                            continue;
                        }
                        if(bigrams[16][9]!=0){
                            continue;
                        }if(bigrams[26][26]!=0){
                            continue;
                        }if(bigrams[21][9]!=0){
                            continue;
                        }
                        if(bigrams[20][9]!=0){
                            continue;
                        }
                        if(bigrams[22][9]!=0){
                            continue;
                        }
                        if(bigrams[23][9]!=0){
                            continue;
                        }
                        if(bigrams[24][9]!=0){
                            continue;
                        }
                        if(bigrams[25][9]!=0){
                            continue;
                        }
                        System.out.println(res[i0][0]+" "+res[i0][1]);

                        System.out.println(rest);
                    }
                }
            }
        }
        /*for(int i =1;i<m*m;i++){
            for(int j =0;j<m*m;j++){

                String rest = decrText(text03, i, j, m, alp);
                for(int i0 =0;i0<m;i0++){
                    for(int j0 =0;j0<m;j0++){
                        bigrams[i0][j0]=0;
                    }
                }
                readBigrams(rest,alp,bigrams,m);
                if(bigrams[0][27]!=0){

                    continue;

                }
                if(bigrams[29][27]!=0){
                    continue;
                }
                if(bigrams[30][27]!=0){
                    continue;
                }
                if(bigrams[14][27]!=0){
                    continue;
                }
                if(bigrams[8][27]!=0){
                    continue;
                }
                if(bigrams[5][27]!=0){
                    continue;
                }
                if(bigrams[1][9]!=0){
                    continue;
                }
                if(bigrams[2][9]!=0){
                    continue;
                }
                if(bigrams[3][9]!=0){
                    continue;
                }
                if(bigrams[7][9]!=0){
                    continue;
                }
                if(bigrams[6][9]!=0){
                    continue;
                }
                if(bigrams[10][9]!=0){
                    continue;
                }
                if(bigrams[11][9]!=0){
                    continue;
                }
                if(bigrams[13][9]!=0){
                    continue;
                }
                if(bigrams[12][9]!=0){
                    continue;
                }
                if(bigrams[18][9]!=0){
                    continue;
                }
                if(bigrams[17][9]!=0){
                    continue;
                }
                if(bigrams[16][9]!=0){
                    continue;
                }if(bigrams[26][26]!=0){
                    continue;
                }if(bigrams[21][9]!=0){
                    continue;
                }
                if(bigrams[20][9]!=0){
                    continue;
                }
                if(bigrams[22][9]!=0){
                    continue;
                }
                if(bigrams[23][9]!=0){
                    continue;
                }
                if(bigrams[24][9]!=0){
                    continue;
                }
                if(bigrams[25][9]!=0){
                    continue;
                }
                System.out.println(i+" "+j);

                System.out.println(rest);
            }
        }
        /*
        String s = readFile("txt.txt",alp);
        System.out.println(s);
        s = encrText(s,5,8,m,alp);
        System.out.println(s);
        s = decrText(s,5,8,m,alp);
        System.out.println(s);*/


    }
}
