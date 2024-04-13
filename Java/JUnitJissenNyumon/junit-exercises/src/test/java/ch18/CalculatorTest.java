package ch18;

import org.junit.Test;

public class CalculatorTest {

    @Test(expected = IllegalArgumentException.class)
    public void divideTest() throws Exception {
        Calculator sut = new Calculator();
        sut.divide(1, 0);
    }

}
