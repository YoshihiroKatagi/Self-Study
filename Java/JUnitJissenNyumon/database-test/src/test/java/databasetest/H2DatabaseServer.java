package databasetest;

import org.junit.rules.ExternalResource;

public class H2DatabaseServer extends ExternalResource {

    private final String baseDir;
    private final String dbName;
    private final String schemaName;
    private Server server = null;

}
