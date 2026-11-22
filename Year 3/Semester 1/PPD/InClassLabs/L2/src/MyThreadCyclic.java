public class MyThreadCyclic extends Thread{
    private double[] a, b, c;
    private int p, tid;
    public MyThreadCyclic(double[] a, double[] b, double[] c, int p, int tid) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.p = p;
        this.tid = tid;
    }

    @Override
    public void run(){
        for(int i = tid; i < a.length; i+=p){
            c[i] = a[i] + b[i];
        }
    }
}
