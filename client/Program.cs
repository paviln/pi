using System;
using System.Net.Http;
using System.Net.Sockets;
using System.Text;

namespace client
{
    class Program
    {
        static TcpClient client;
        static System.Threading.Tasks.Task Main(string[] args)
        {
            while (true)
            {
                try
                {
                    string serverIP = "192.168.1.200";
                    int port = 5560;
                    client = new TcpClient(serverIP, port);
                    NetworkStream stream = client.GetStream();
                    System.Console.Write("Command: ");
                    string command = Console.ReadLine();
                    Byte[] sendBytes = Encoding.UTF8.GetBytes(command);
                    stream.Write(sendBytes, 0, sendBytes.Length);
                }
                catch (HttpRequestException e)
                {
                    Console.WriteLine("\nException Caught!");
                    Console.WriteLine("Message :{0} ", e.Message);
                }
            }
        }
    }
}
