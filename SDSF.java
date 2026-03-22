import java.util.Scanner;

public class SDSF {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        String s = sc.next();
        if(s.matches("\\d+")) {
            long start = System.nanoTime();
            long total = 0;
            for (char c : s.toCharArray()) total += (c - '0');
            long res = (total == 0) ? 0 : 1 + (total - 1) % 9;
            long end = System.nanoTime();
            System.out.println("Result: " + res + " | Time: " + (end-start)/1000000.0 + "ms");
        }
    }
}
