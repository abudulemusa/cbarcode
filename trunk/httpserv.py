#!/usr/bin/python
import BaseHTTPServer
import SimpleHTTPServer
import CGIHTTPServer
import sys

# Run a simple HTTP server on the loopback interface on port 8080.
# 
# Put CGI Scripts in directory /cgi
#
def runServer(args):
    if "-a" in args:
        serverAddress = ('', 8080)
    else:
        serverAddress = ('127.0.0.1', 8080)

    handlerClass = CGIHTTPServer.CGIHTTPRequestHandler
    handlerClass.cgi_directories = ['/cgi-bin']
    serverClass  = BaseHTTPServer.HTTPServer

    httpd = serverClass(serverAddress, handlerClass)
    sa = httpd.socket.getsockname()

    print "Development web server starting ...\n"
    print "Point your web browser at: http://127.0.0.1:%d/\n" % sa[1]
    print "Type CTRL+C top stop the web server.\n"

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print "Development web server stopped!"


# If called from the command line start up the server.
if __name__ == '__main__':
    if "-h" in sys.argv:

        print "Usage: %s [OPTIONS]" % sysv.argv[0]
        print "    -a Listen on all ip addresses (default is loopback only)."
        print "    -h Print this help message."
        sys.exit(0)

    else:
        runServer(sys.argv)