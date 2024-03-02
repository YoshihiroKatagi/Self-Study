package junit.example.ch04;

import org.junit.Ignore;
import org.junit.Test;

import java.util.Date;

import static junit.example.ch04.IsDate.*;
import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

@Ignore
public class IsDateTest {

    @Test
    public void CompareWithDate() throws Exception {
        Date date = new Date();
        assertThat(date, is(dateOf(2011, 2, 10)));
    }

    @Test
    public void CompareWithNull() throws Exception {
        assertThat(null, is(dateOf(2011, 2, 10)));
    }
}