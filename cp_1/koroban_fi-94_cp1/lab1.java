import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void readFile(String fname,double[] l0,double[]l1, double[][] b01,double[][]b02,double[][]b11,double[][]b12,int m1,int m2){
        try(FileReader reader = new FileReader(fname))
        {
            int calcl0 = 0;
            int calcl1 = 0;
            int calcb02 = 0;
            int calcb01 = 0;
            int calcb12 = 0;
            int calcb11 = 0;
            int c;
            int space = 0;
            int indexPrev =-1;
            int indexPrev2 =-1;
            int indStep = 0;

            while((c=reader.read())!=-1){
                if(indStep>1){
                    indStep=0;
                }
                int tempc = Character.toLowerCase(c)-1072;
                int tempIndex = 0;
                if(tempc>=0&&tempc<32){
                    tempIndex=tempc;
                    space=0;
                }else if(tempc==33){
                    tempIndex = 32;
                    space=0;
                }
                else{
                    tempIndex= 33;
                }

                if(tempIndex<33){
                    l0[tempIndex]++;
                    calcl0++;
                    if(indexPrev>0&&indexPrev<33){
                        b01[indexPrev][tempIndex]++;
                        calcb01++;
                    }
                    if(indexPrev>0&&indexPrev<33&&indStep==1){
                        b02[indexPrev2][tempIndex]++;
                        calcb02++;
                    }
                }
                if(space==0){
                    l1[tempIndex]++;
                    calcl1++;
                    if(indexPrev>0){
                        b11[indexPrev][tempIndex]++;
                        calcb11++;
                    }
                    if(indexPrev>0&&indStep==1){
                        b12[indexPrev2][tempIndex]++;
                        calcb12++;
                    }
                }







                if(space==0){
                    if(indStep==0){
                        indexPrev2=tempIndex;
                    }
                    indStep++;
                    indexPrev = tempIndex;
                }
                if(!(tempc>=0&&tempc<32)&&!(tempc==33)){
                    space=1;
                }

            }
            for(int i=0;i<m1;i++){
                l0[i]=l0[i]/calcl0;
                for(int j =0;j<m1;j++){
                    b01[i][j]=b01[i][j]/calcb01;
                    b02[i][j]=b02[i][j]/calcb02;
                }
            }
            for(int i=0;i<m2;i++){
                l1[i]=l1[i]/calcl1;
                for(int j =0;j<m2;j++){
                    b11[i][j]=b11[i][j]/calcb11;
                    b12[i][j]=b12[i][j]/calcb12;
                }
            }
        }
        catch(IOException ex){

            System.out.println(ex.getMessage());
        }

    }

    public static void main(String[] args){
        for(int i =1072;i<1104;i++){
            System.out.println(i+" = "+(char)i+ " = "+i%1072);
        }
        String fname = "text00.txt";
        int m1 = 33;
        int m2 = 34;
        double[][] bigrams = new double[m1][m1];
        double[][] bigramsIntersect = new double[m1][m1];
        double[][] bigramsWithSpaces = new double[m2][m2];
        double[][] bigramsWithSpacesIntersect = new double[m2][m2];
        double[] lettes = new double[m1];
        double[] lettersWithSpaces = new double[m2];
        for(int i=0;i<m1;i++){
            lettes[i]=0.0;
            for(int j=0;j<m1;j++){
                bigrams[i][j]=0.0;
            }
        }
        for(int i=0;i<m2;i++){
            lettersWithSpaces[i]=0.0;
            for(int j=0;j<m2;j++){
                bigramsWithSpaces[i][j]=0.0;
            }
        }
        readFile(fname,lettes,lettersWithSpaces,bigramsIntersect,bigrams,bigramsWithSpaces,bigramsWithSpacesIntersect,m1,m2);

        double sum = 0;
        double max =0;
        double imax =-1;
        for(int i=0;i<m1;i++){
            sum+=lettes[i];
            double tempmax = max;
            double tempi = imax;
            max =0;
            imax = -1;
            for(int i0 =0;i0<m1;i0++){
                if(i==0){
                    if(max<lettes[i0]){
                        max = lettes[i0];
                        imax = i0;
                    }
                }else{
                    if(max<lettes[i0]&&(lettes[i0]<=tempmax&&i0!=tempi)){
                        max = lettes[i0];
                        imax = i0;
                    }

                }
            }
            if(imax!=32){
                System.out.println((char) (1072+imax)+" "+max);
            }else{
                System.out.println('ё'+" "+max);
            }

        }
        max =0;
        imax = -1;
        sum = 0;
        for(int i=0;i<m2;i++){
            sum+=lettersWithSpaces[i];
            double tempmax = max;
            double tempi = imax;
            max =0;
            imax = -1;
            for(int i0 =0;i0<m2;i0++){
                if(i==0){
                    if(max<lettersWithSpaces[i0]){
                        max = lettersWithSpaces[i0];
                        imax = i0;
                    }
                }else{
                    if(max<lettersWithSpaces[i0]&&(lettersWithSpaces[i0]<=tempmax&&i0!=tempi)){
                        max = lettersWithSpaces[i0];
                        imax = i0;
                    }

                }
            }
            if(imax<32){
                System.out.println((char) (1072+imax)+" "+max);
            }else if(imax==32){
                System.out.println('ё'+" "+max);
            }
            else{
                System.out.println(' '+" "+max);
            }
        }
        for(int i =-1;i<m1;i++){
            if(i==-1){
                System.out.println("  ");
            }else if(i!=32){
                System.out.print((char)(1072+i)+" ");
            }else{
                System.out.print('ё'+" ");
            }
            for(int j = 0;j<m1;j++){
                if(i==-1){
                    if(j!=32){
                        System.out.print("    "+(char)(1072+j)+"  ");
                    }else{
                        System.out.print("    "+'ё'+" ");
                    }
                }else{
                    String temp = String.format("%.4f",bigrams[i][j]);
                    System.out.print(temp+" ");
                }
            }
            if(0<=i&&i<32){
                System.out.print((char)(1072+i)+" ");
            }else if(i==32){
                System.out.print('ё'+" ");
            }else{
                System.out.print("  ");
            }
            System.out.println();
        }
        for(int i =-1;i<m1;i++){
            if(i==-1){
                System.out.println("  ");
            }else if(i!=32){
                System.out.print((char)(1072+i)+" ");
            }else{
                System.out.print('ё'+" ");
            }
            for(int j = 0;j<m1;j++){
                if(i==-1){
                    if(j!=32){
                        System.out.print("    "+(char)(1072+j)+"  ");
                    }else{
                        System.out.print("    "+'ё'+" ");
                    }
                }else{
                    String temp = String.format("%.4f",bigramsIntersect[i][j]);
                    System.out.print(temp+" ");
                }
            }
            if(0<=i&&i<32){
                System.out.print((char)(1072+i)+" ");
            }else if(i==32){
                System.out.print('ё'+" ");
            }else{
                System.out.print("  ");
            }
            System.out.println();
        }
        for(int i =-1;i<m2;i++){
            if(i==-1){
                System.out.println("  ");
            }else if(i<32){
                System.out.print((char)(1072+i)+" ");
            }else if(i==32){
                System.out.print('ё'+" ");
            }else{
                System.out.print("  ");
            }
            for(int j = 0;j<m2;j++){
                if(i==-1){
                    if(j<32){
                        System.out.print("    "+(char)(1072+j)+"  ");
                    }else if(j==32){
                        System.out.print("    "+'ё'+"  ");
                    }else{
                        System.out.print("       ");
                    }

                }else{
                    String temp = String.format("%.4f",bigramsWithSpaces[i][j]);
                    System.out.print(temp+" ");
                }
            }
            if(0<=i&&i<32){
                System.out.print((char)(1072+i)+" ");
            }else if(i==32){
                System.out.print('ё'+" ");
            }else{
                System.out.print("  ");
            }
            System.out.println();
        }

        for(int i =-1;i<m2;i++){
            if(i==-1){
                System.out.println("  ");
            }else if(i<32){
                System.out.print((char)(1072+i)+" ");
            }else if(i==32){
                System.out.print('ё'+" ");
            }else{
                System.out.print("  ");
            }
            for(int j = 0;j<m2;j++){
                if(i==-1){
                    if(j<32){
                        System.out.print("    "+(char)(1072+j)+"  ");
                    }else if(j==32){
                        System.out.print("    "+'ё'+"  ");
                    }else{
                        System.out.print("       ");
                    }

                }else{
                    String temp = String.format("%.4f",bigramsWithSpacesIntersect[i][j]);

                    System.out.print(temp+" ");
                }
            }
            if(0<=i&&i<32){
                System.out.print((char)(1072+i)+" ");
            }else if(i==32){
                System.out.print('ё'+" ");
            }else{
                System.out.print("  ");
            }
            System.out.println();
        }
        double H = 0.0;
        for(int i =0;i<m1;i++){
            H-=lettes[i]*Math.log(lettes[i])/Math.log(2);
        }
        System.out.println(H);
        H = 0.0;
        for(int i =0;i<m2;i++){
            H-=lettersWithSpaces[i]*Math.log(lettersWithSpaces[i])/Math.log(2);
        }
        System.out.println(H);
        H = 0.0;
        for(int i =0;i<m1;i++){
            for(int j=0;j<m1;j++){
                if(bigrams[i][j]!=0.0){
                    H-=bigrams[i][j]*Math.log(bigrams[i][j])/Math.log(2);
                }
            }

        }
        System.out.println(H);
        H = 0.0;
        for(int i =0;i<m1;i++){
            for(int j=0;j<m1;j++){
                if(bigramsIntersect[i][j]!=0.0){
                    H-=bigramsIntersect[i][j]*Math.log(bigramsIntersect[i][j])/Math.log(2);
                }
            }

        }
        System.out.println(H);
        H = 0.0;
        for(int i =0;i<m2;i++){
            for(int j=0;j<m2;j++){
                if(bigramsWithSpaces[i][j]!=0.0){
                    H-=bigramsWithSpaces[i][j]*Math.log(bigramsWithSpaces[i][j])/Math.log(2);
                }
            }

        }
        System.out.println(H);
        H = 0.0;
        for(int i =0;i<m2;i++){
            for(int j=0;j<m2;j++){
                if(bigramsWithSpacesIntersect[i][j]!=0.0){
                    H-=bigramsWithSpacesIntersect[i][j]*Math.log(bigramsWithSpacesIntersect[i][j])/Math.log(2);
                }
            }

        }
        System.out.println(H);
    }
}
