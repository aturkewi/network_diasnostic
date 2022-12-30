import unittest

from check_ping import get_time_string

class CheckPing(unittest.TestCase):
  """Test for ping checking tool"""

  def test_get_time_string(self):
    """Return time from long string"""

    string = "'PING google.com (142.250.65.238): 56 data bytes\n64 bytes from 142.250.65.238: icmp_seq=0 ttl=116 time=29.708 ms\n\n--- google.com ping statistics ---\n1 packets transmitted, 1 packets received, 0.0% packet loss\nround-trip min/avg/max/stddev = 29.708/29.708/29.708/0.000 ms\n'"
    time = get_time_string(string)
    self.assertEqual(time, '29.708')

if __name__ == '__main__':
  unittest.main()
