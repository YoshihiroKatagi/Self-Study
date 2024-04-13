package junit.example.ch06;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;

public class ArrayListFlatTest {

    private ArrayList<String> sut;

    @Before
    public void setUp() throws Exception {
        sut = new ArrayList<String>();
    }

    @Test
    public void InCaseItHasOneDataInList_sizeReturnes1() throws Exception {
        sut.add("A");
        int actual = sut.size();
        assertThat(actual, is(1));
    }

    @Test
    public void InCaseItHasTwoDataInList_sizeReturnes2() throws Exception {
        sut.add("A");
        sut.add("B");
        int actual = sut.size();
        assertThat(actual, is(2));
    }
}
