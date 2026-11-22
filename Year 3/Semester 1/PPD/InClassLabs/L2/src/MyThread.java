public class MyThread extends Thread{
    private double[] a, b, c;
    private int begin, end;
    public MyThread(double[] a, double[] b, double[] c, int begin, int end) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.begin = begin;
        this.end = end;
    }

    @Override
    public void run(){
        for(int i = begin; i < end; i++){
            c[i] = a[i] + b[i];
        }
    }
}
