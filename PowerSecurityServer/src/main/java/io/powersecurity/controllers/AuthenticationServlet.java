package io.powersecurity.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("/login")
public class AuthenticationServlet {
	
	private final static String CONTROLLER_NAME = "Authentication";
	
	private final static String LOGIN_JSP = "login";
	
	
	@GetMapping
	public ModelAndView getPage() {
		ModelAndView model = new ModelAndView(LOGIN_JSP);
		model.addObject("service",CONTROLLER_NAME);
		return model;
	}
}
