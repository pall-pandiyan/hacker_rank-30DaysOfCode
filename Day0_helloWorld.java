import java.io.*;
import java.util.*;

public class Day0_helloWorld {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        String inputString = scan.nextLine();
        System.out.println("Hello, World.");
        System.out.println(inputString);
        scan.close();
    }
}