package io.powersecurity.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("/login")
public class AuthenticationServlet {
	
	@GetMapping
	public ModelAndView getPage() {
		return new ModelAndView("index");
	}
}
