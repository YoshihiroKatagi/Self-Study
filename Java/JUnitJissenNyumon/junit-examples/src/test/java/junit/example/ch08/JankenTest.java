package junit.example.ch08;

import org.junit.Before;
import org.junit.Test;

import static junit.example.ch08.Janken.Hand.*;
import static junit.example.ch08.Janken.Result.*;
import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

public class JankenTest {

    private Janken sut;

    @Before
    public void setUp() throws Exception {
        sut = new Janken();
    }

    @Test
    public void WinWithGuAndTyoki() throws Exception {
        assertThat(sut.judge(GU, TYOKI), is(WIN));
    }

    @Test
    public void LoseWithGuAndPa() throws Exception {
        assertThat(sut.judge(GU, PA), is(LOSE));
    }

    @Test
    public void DrawWithGuAndGu() throws Exception {
        assertThat(sut.judge(GU, GU), is(DRAW));
    }

    @Test
    public void WinWithTyokiAndPa() throws Exception {
        assertThat(sut.judge(TYOKI, PA), is(WIN));
    }
}
