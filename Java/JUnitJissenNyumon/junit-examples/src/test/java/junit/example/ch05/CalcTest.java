package junit.example.ch05;

import org.junit.Test;
import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

public class CalcTest {

    @Test
    public void TestAdd_with3plus4equal7 () {
        Calc sut = new Calc();
        assertThat(sut.add(3, 4), is(7));
    }

    public static void main(String[] args) {
        org.junit.runner.JUnitCore.main(CalcTest.class.getName());
    }
}
