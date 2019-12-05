#include <iostream>
#include <ivi-logging/ivi-logging.h>

typedef logging::DefaultLogContext LogContext;

// If an application is not multi-instance, we can define its unique identifier
LOG_DEFINE_APP_IDS("MyAp", "This is a small application showing how to use ivi-logging");

// Instantiate a log context and define it as default for this module
LOG_DECLARE_DEFAULT_CONTEXT(mainContext, "MAIN", "This is a description of that logging context");

int main() {

    log_debug() << "Testing ivi-logging";

    return 0;
}
