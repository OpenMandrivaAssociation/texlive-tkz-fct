%global tl_name tkz-fct
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7c
Release:	%{tl_revision}.1
Summary:	Tools for drawing graphs of functions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-fct
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-fct.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-fct.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The tkz-fct package is designed to give math teachers (and students)
easy access to programming graphs of functions with TikZ and gnuplot.

