package junit.example.ch11;

import java.util.Date;

public class MethodExtractExample {
    Date date = newDate();

    public void doSomething() {
        this.date = newDate();
        // なんらかの処理（省略）
    }

    Date newDate() {
        return new Date();
    }
}
