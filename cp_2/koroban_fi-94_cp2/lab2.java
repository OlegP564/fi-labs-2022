import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    public static void readFile2(String fname,double[] l0,int m1){
        try(FileReader reader = new FileReader(fname))
        {
            int calcl0 = 0;

            int c;

            while((c=reader.read())!=-1){

                int tempc = Character.toLowerCase(c)-1072;
                int tempIndex = -1;
                if(tempc>=0&&tempc<32){
                    tempIndex=tempc;
                }
                if(tempIndex>=0){
                    l0[tempIndex]++;
                    calcl0++;

                }

            }
            for(int i=0;i<m1;i++){
                l0[i]=l0[i]/calcl0;

            }

        }
        catch(IOException ex){

            System.out.println(ex.getMessage());
        }

    }

    public static String readFile(String fname,int[]letters){
        String text ="";
        ArrayList<Integer> alp = new ArrayList<Integer>();
        for(int i=0;i<letters.length;i++){
            alp.add(letters[i]);
        }
        try(FileReader reader = new FileReader(fname))
        {

            int c;
            while((c=reader.read())!=-1){
                if(alp.contains((int)Character.toLowerCase(c))){
                    text+=(char)c;
                }

            }
        }
        catch(IOException ex){

            System.out.println(ex.getMessage());
        }
        return text;
    }
    public static double matchingIndex(String txt,int[]letters, int m){
        double mIndex =0.0;
        int [][] arr = new int[m][2];
        int n = txt.length();
        for(int i =0;i<m;i++){
            arr[i][0]=letters[i];
            arr[i][1]=0;
        }
        for(int i=0;i<txt.length();i++){
            for(int j=0;j<m;j++){
                if(arr[j][0]==(int)Character.toLowerCase(txt.charAt(i)))
                {
                    arr[j][1]++;
                    break;
                }
            }
        }
        for(int i =0;i<m;i++){

            mIndex+=((double)1/(double)n/(n-1))*arr[i][1]*(arr[i][1]-1);
        }
        return mIndex;
    }
    public static String encryptText(int []kr,int r,String text,int[]letters,int m){
        String res ="";
        String txt2 = "";
        int i0 = -1;
        for(int i =0;i<text.length();i++){
            int j0=-1;
            for(int j=0;j<m;j++){
                if(letters[j]==(int)Character.toLowerCase(text.charAt(i))){
                    j0=j;  i0++;
                    break;

                }
            }
            if(j0>=0) {
                int temp =letters[j0] + kr[i0 % r];
                temp-=1072*2;
                if(temp <0){
                    temp+=1072;
                }
                if(temp <0){
                    temp+=1072;
                }

                res += (char) (letters[(temp) %m]);
            }
        }
        return res;
    }
    public static int kronekerSymbol(String text,int r){
        int res = 0;
        for(int i =0;i<text.length()-r;i++){
            if(text.charAt(i)==text.charAt(i+r)){
                res++;
            }
        }
        return res;
    }
    public static int decrCesar(String text,int most,int[] letters,int m){
        int ki =0;
        int [][] arr = new int[m][2];
        int n = text.length();
        for(int i =0;i<m;i++){
            arr[i][0]=letters[i];
            arr[i][1]=0;
        }
        for(int i=0;i<text.length();i++){
            for(int j=0;j<m;j++){
                if(arr[j][0]==(int)Character.toLowerCase(text.charAt(i)))
                {
                    arr[j][1]++;
                    break;
                }
            }
        }
        int max = 0;
        int maxi = -1;
        for(int i =0;i<m;i++){
            if(max <= arr[i][1]){
                max = arr[i][1];
                maxi=arr[i][0];
            }
        }
        int ind = maxi-most;
        if (ind<0){
            ind += m;
        }
        ki = letters[ind%m];

        return ki;
    }
    public static String decrText(String text,int []ki,int []letters,int m,int r){
        String res ="";
        for(int i =0;i<text.length();i++){
            int j0=-1;
            for(int j=0;j<m;j++){
                if(letters[j]==(int)Character.toLowerCase(text.charAt(i))){
                    j0=j;
                    break;
                }
            }
            if(j0>=0) {
                int temp =letters[j0]%1072 - ki[i % r]%1072;
                if(temp<0){
                    temp+=m;
                }
                if(temp <0){
                    temp+=1072;
                }
                res += (char) (letters[temp %m]);
            }
        }
        return res;
    }
    public static int Mig(String txt,int []letters, int m,double []p){

        int [][] arr = new int[m][2];
        int n = txt.length();
        for(int i =0;i<m;i++){
            arr[i][0]=letters[i];
            arr[i][1]=0;
        }
        for(int i=0;i<txt.length();i++){
            for(int j=0;j<m;j++){
                if(arr[j][0]==(int)Character.toLowerCase(txt.charAt(i)))
                {
                    arr[j][1]++;
                    break;
                }
            }
        }

        double max = 0;
        int maxi =-1;
        for(int g =0;g<m;g++) {
            double temp =0;
            for(int i =0;i<m;i++){
                temp +=  p[i] * arr[(i + g) % m][1];

            }
            //System.out.print(Math.round(temp)+ " ");
            System.out.println(g);
            System.out.println(temp);
            if(max<=temp){
                maxi = g;
                max = temp;
            }

        }
        //System.out.println();
        return letters[maxi];
    }

    public static void main(String []args){
        String ciphertext ="";
        String texttocipher = "";
        String fname = "text.txt";
        String fname2 = "text2.txt";
        String fname3 = "text0.txt";
        int mm1 = 32;
        double[] lettes = new double[mm1];

        for(int i=0;i<mm1;i++){
            lettes[i]=0.0;
        }
        readFile2(fname3,lettes,mm1);


        int m = 32;
        int m2 = 33;
        int []alphabet = new int[m];
        int []alphabet2 = new int[m2];

        char a0 = 'а';
        for(int i =0;i<m;i++){
            alphabet[i]=(int)a0;
            alphabet2[i]=(int)a0;
            a0++;
        }
        alphabet2[m2-1]=14;
        ciphertext = readFile(fname,alphabet);
        texttocipher = readFile(fname2,alphabet2);
        double I0 = matchingIndex(ciphertext,alphabet,m);
        System.out.println(I0);
        System.out.print("Matching index for open text = ");
        System.out.println(matchingIndex(texttocipher,alphabet2,m2));
        int r1 = 2;
        int[]kr1 = new int[] {1072,1073};
        for(int i =2;i<21;i++){
            int r = i;
            //System.out.println("for key length "+r);
            System.out.print("for key: [");
            int[]kr = new int[r];
            ArrayList<Integer> visited = new ArrayList<Integer>();
            for(int j=0;j<r;j++){
                int temp =(int)(Math.random()*(31)+1072);
                while (visited.contains(temp)){
                    temp =(int)(Math.random()*(31)+1072);
                }
                kr[j]= temp;
                visited.add(temp);

                if(j!=r-1) {
                    System.out.print(kr[j] + "; ");
                }else{
                    System.out.print(kr[j]);
                }
            }
            System.out.println("]");
            System.out.print("Mathcing index = ");
            System.out.println(matchingIndex(encryptText(kr,r,texttocipher,alphabet2,m2),alphabet2,m2));
            System.out.println();

        }

        System.out.println();
        int n = ciphertext.length();
        for(int i = 2;i<30;i++){
            System.out.println("for r = "+i+" Dr = "+kronekerSymbol(ciphertext,i));
        }
        int r =14;

        String[] arr = new String[r];
        for (int j = 0; j < r; j++) {
            arr[j] = "";
        }
        for (int i0 = 0; i0 < (int) (n / r) - r; i0++) {
            for (int j = 0; j < r; j++) {
                arr[j] += ciphertext.charAt(i0 * r + j);
            }
        }
        int[] kires = new int[r];
        for (int i = 0; i < r; i++) {
            kires[i] = decrCesar(arr[i], (int) 'о', alphabet, m);
            System.out.print((char) kires[i] + " ");
        }
        System.out.println();
        System.out.println(decrText(ciphertext, kires, alphabet, m, r));
        for (int i = 0; i < r; i++) {
            //System.out.println(arr[i]);
            kires[i] = Mig(arr[i], alphabet, m, lettes);
            System.out.print((char) kires[i] + " ");
        }
        System.out.println();

        System.out.println(decrText(ciphertext, kires, alphabet, m, r));
        /*int []test = {1079, 1086, 1090, 1089};
        System.out.println();
        System.out.println(decrText(encryptText(test,4,texttocipher,alphabet,m),test,alphabet,m,4));*/



    }
}
