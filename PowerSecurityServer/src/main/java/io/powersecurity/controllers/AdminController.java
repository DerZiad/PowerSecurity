package io.powersecurity.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;

import io.powersecurity.models.Entry;
import io.powersecurity.services.EntriesService;

@RestController
@RequestMapping("/admin")
public class AdminController {
	
	private EntriesService entryService;
	
	@GetMapping
	public ModelAndView getPageAdmin() {
		return new ModelAndView("index");
	}
	
	@GetMapping("/searchEntry")
	public ModelAndView searchEntry(@RequestPayload Entry entry) {
		
		return null;
	}
	

}
