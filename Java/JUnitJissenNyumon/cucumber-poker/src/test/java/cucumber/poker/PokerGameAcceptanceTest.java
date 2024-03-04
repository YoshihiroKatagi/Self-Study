package cucumber.poker;

import cucumber.junit.Cucumber;
import org.junit.runner.RunWith;
import cucumber.runtime.*;

@RunWith(Cucumber.class)
@Cucumber.Options(format = {"pretty"}, monochrome = true)
public class PokerGameAcceptanceTest {

    public void distributed_in_hand_S_H_D_D_C(
            int arg1, int arg2, int arg3, int arg4, int arg5) throws Throwable {
        throw new PendingException();
    }

    public void not_change_hand() throws Throwable {
        throw new PendingException();
    }

    public void should_be_no_pair() throws Throwable {
        throw new PendingException();
    }
}
