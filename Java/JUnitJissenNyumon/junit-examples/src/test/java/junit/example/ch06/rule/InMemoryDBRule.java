package junit.example.ch06.rule;

import junit.example.ch06.withoutrule.InMemoryDB;
import org.junit.rules.TestRule;
import org.junit.runner.Description;
import org.junit.runners.model.Statement;

public class InMemoryDBRule implements TestRule {

    InMemoryDB db = null;

    @Override
    public Statement apply(final Statement base, Description description) {
        db = new InMemoryDB();
        return new Statement() {

            @Override
            public void evaluate() throws Throwable {
                db.start();
                try {
                    base.evaluate();
                } finally {
                    db.shutdownNow();
                }
            }
        };
    }
}
