package io.powersecurity.filters;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.core.annotation.Order;
import org.springframework.security.authentication.AnonymousAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;

@Order(1)
public class SessionFilter implements Filter {
	@Override
	public void init(FilterConfig filterConfig) throws ServletException {
	}

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
			throws IOException, ServletException {
		HttpServletRequest req = (HttpServletRequest) request;
		HttpServletResponse resp = (HttpServletResponse) response;
		String path = req.getServletPath();
		Authentication authentication = SecurityContextHolder.getContext().getAuthentication();

		boolean testRessource = false;
		List<String> list = Arrays.asList("/assets");

		for (String item : list) {
			if (path.startsWith(item)) {
				testRessource = true;
			}
		}

		/**
		 * 
		 * I did if else and not else if because i doesn t to do a long traitment for
		 * ressoucres
		 **/

		if (testRessource) {
			chain.doFilter(req, resp);
		} else {
			if(path.startsWith("/login")) {
				if(!(authentication instanceof AnonymousAuthenticationToken)) {
					resp.sendRedirect("/admin");
				}else {
					chain.doFilter(request, response);
				}
			}else if(path.startsWith("/logout")) {
				if(!(authentication instanceof AnonymousAuthenticationToken)) {
					resp.sendRedirect("/login");
				}else {
					chain.doFilter(request, response);
				}
			}else if(path.startsWith("/admin")) {
				if(authentication instanceof AnonymousAuthenticationToken) {
					resp.sendRedirect("/login");
				}else {
					chain.doFilter(request, response);
				}
			}else if(path.equals("/")) {
				if(authentication instanceof AnonymousAuthenticationToken) {
					resp.sendRedirect("/login");
				}else {
					resp.sendRedirect("/admin");
				}
			}
		}
	}
}