#!/usr/bin/env python
# -*- coding: utf-8 -*-

tests = 
{
	'x_is_negative': 	
	{
		'value':-5, 
		'__doc__': 'Negative X', 
		'expected': 'error'
	},
	'x_is_zero': 		
	{
		'value':0, 
		'__doc__': 'X = 0', 
		'expected': 1
	},
	'x_is_one': 		
	{
		'value':1, 
		'__doc__': 'X = 1', 
		'expected': 1
	},
	'x_is_positive': 	
	{
		'value':5, 
		'__doc__': 'Positive X', 
		'expected': 120
	}
}
