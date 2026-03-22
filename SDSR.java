import java.util.Scanner;

public class SDSR {
    static int getSum(String n) {
        if (n.length() == 1) return n.charAt(0) - '0';
        long sum = 0;
        for (char c : n.toCharArray()) sum += (c - '0');
        return getSum(String.valueOf(sum));
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number: ");
        String s = sc.next();
        if(s.matches("\\d+")) {
            long start = System.nanoTime();
            int res = getSum(s);
            long end = System.nanoTime();
            System.out.println("Result: " + res + " | Time: " + (end-start)/1000000.0 + " MS ");
        } else { System.out.println("Invalid Input!"); }
    }
}
