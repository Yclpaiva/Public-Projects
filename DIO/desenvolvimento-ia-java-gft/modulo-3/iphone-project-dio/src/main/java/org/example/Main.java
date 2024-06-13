package org.example;

import org.example.iphone.phone;
import org.example.iphone.CPUs;

public class Main {
    public static void main(String[] args) {

        phone Iphone11 = new phone();
        Iphone11.setCpu(CPUs.A13_BIONIC.toString());
        Iphone11.setRam(4);
        Iphone11.setStorage(128);
        Iphone11.setColor("Black");

        System.out.println(Iphone11.getSpecs());
    }
}