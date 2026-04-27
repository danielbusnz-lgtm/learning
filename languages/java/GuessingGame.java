import java.util.Scanner;
import java.util.Random;

public class GuessingGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random rand = new Random();
        int n = rand.nextInt(100); 
       
        int guess = -1;
        int count = 0;

        System.out.println("Guess Game Starting");
  
    while (guess != n){
        System.out.println("Enter Your Guess");
        count ++;
        guess=  scanner.nextInt();

        if (guess > n){
                System.out.println("You Guessed too High");
        } else if (guess < n){
                System.out.println("You Guess too low");
        } 
               
        }
        System.out.println("Correct! It took you  " + count +" tries!");

}
}
