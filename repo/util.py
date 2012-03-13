def str2bool(v):
	if v is None:
		return None
	
	if v.lower() in ("yes", "true", "t", "1"):
		return True
	elif v.lower() in ("no", "false", "f", "0"):
		return False
	else:
		return v