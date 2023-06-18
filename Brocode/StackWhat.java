package Brocode;

import java.util.*;

public class StackWhat {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<String>();

        System.out.println(stack.isEmpty());

        stack.push("Minecraft");
        stack.push("Fortnite");
        stack.push("Roblox");
        stack.push("Among Us");
        stack.push("Call of Duty");
        stack.push("Apex Legends");

        System.out.println(stack.peek());

        stack.pop();

        System.out.println(stack.search("Minecraft"));
        System.out.println("Stack: " + stack);
    }
}