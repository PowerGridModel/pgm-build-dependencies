/* Copyright (c) 2018-2024 Marcelo Zimbres Silva (mzimbres@gmail.com)
 *
 * Distributed under the Boost Software License, Version 1.0. (See
 * accompanying file LICENSE.txt)
 */

#include <boost/redis/connection.hpp>
#include <cstddef>

namespace boost::redis {

connection::connection(
   executor_type ex,
   asio::ssl::context ctx,
   std::size_t max_read_size)
: impl_{ex, std::move(ctx), max_read_size}
{ }

connection::connection(
   asio::io_context& ioc,
   asio::ssl::context ctx,
   std::size_t max_read_size)
: impl_{ioc.get_executor(), std::move(ctx), max_read_size}
{ }

void
connection::async_run_impl(
   config const& cfg,
   logger l,
   asio::any_completion_handler<void(boost::system::error_code)> token)
{
   impl_.async_run(cfg, l, std::move(token));
}

void
connection::async_exec_impl(
   request const& req,
   any_adapter&& adapter,
   asio::any_completion_handler<void(boost::system::error_code, std::size_t)> token)
{
   impl_.async_exec(req, std::move(adapter), std::move(token));
}

void connection::cancel(operation op)
{
   impl_.cancel(op);
}

} // namespace boost::redis
