import java.io.*;
import java.util.*;

public class Day01_dataTypes {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int i=4;
        double d=4.0;
        String s="HackerRank ";
        
        int i2;
        double d2;
        String s2;
        
        Scanner scan = new Scanner(System.in);
        i2 = Integer.parseInt(scan.nextLine());
        d2 = Double.parseDouble(scan.nextLine());
        s2 = scan.nextLine();
        scan.close();
        i += i2;
        d += d2;
        s += s2;
        
        System.out.println(i);
        System.out.println(d);
        System.out.println(s);
    }
}