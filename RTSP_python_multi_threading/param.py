import argparse

def get_parser():
	parser = argparse.ArgumentParser()

	parser.add_argument("--fps", type=int, default=10)
	
	# RTSP
	parser.add_argument("--ip", type=str)
	parser.add_argument("--port", type=str)
	parser.add_argument("--path", type=str)
	parser.add_argument("--id", type=str, default='None')
	parser.add_argument("--password", type=str, default='None')
	parser.add_argument("--rtsp_transport", type=str, default='udp')
	parser.add_argument("--buffer_size", type=str, default='425984')
	parser.add_argument("--stimeout", type=str, default='200000')
	parser.add_argument("--max_delay", type=str, default='200000')
	
	# Img
	parser.add_argument("--img_width", type=int, default=2048)
	parser.add_argument("--img_height", type=int, default=2048)	

	# Frame queue
	parser.add_argument("--max_size", type=int, default=-1)
	parser.add_argument("--skip_count", type=int, default=1)
	
	# Web server
	parser.add_argument("--activate_web_server", action="store_true")
	parser.add_argument("--browser_path", type=str, default='/usr/bin/google-chrome %s')
	parser.add_argument("--web_server_host", type=str, default='0.0.0.0')
	parser.add_argument("--web_server_port", type=int, default=5000)
	
	return parser.parse_args()
