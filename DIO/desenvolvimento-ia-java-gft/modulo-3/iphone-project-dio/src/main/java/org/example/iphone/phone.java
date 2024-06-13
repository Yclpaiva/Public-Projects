package org.example.iphone;

public class phone {

    private String cpu;
    private int ram;
    private int storage;
    private String color;

    public void setCpu(String cpu) {
        this.cpu = cpu;
    }

    public void setRam(int ram) {
        this.ram = ram;
    }

    public void setStorage(int storage) {
        this.storage = storage;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getCpu() {
        return cpu;
    }

    public int getRam() {
        return ram;
    }

    public int getStorage() {
        return storage;
    }

    public String getColor() {
        return color;
    }

    public String getSpecs() {
        return "CPU: " + cpu + "\n" +
               "RAM: " + ram + "GB\n" +
               "Storage: " + storage + "GB\n" +
               "Color: " + color;
    }

}
