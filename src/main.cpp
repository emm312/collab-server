#include "boost/asio/detail/chrono.hpp"
#include "boost/asio/execution_context.hpp"
#include "boost/asio/io_context.hpp"
#include "boost/asio/steady_timer.hpp"
#include <iostream>
#include <string>
#include <boost/asio.hpp>
#include <boost/coroutine2/coroutine.hpp>
// Time to figure out how boost works
int main() {
    boost::asio::io_context io;
    boost::asio::steady_timer t(io, boost::asio::chrono::seconds(5));
    t.wait();

    std::cout << "Hello World" << std::endl;
    return 0;
}